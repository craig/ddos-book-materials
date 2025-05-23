package main

import (
 "crypto/tls"
 "log"
 "time"
 "unsafe"

 "golang.org/x/net/http2"
)

func main() {
 host := "www.cloudflare.com"

 tcfg := &tls.Config{
  NextProtos: []string{
   "h2",
  },
  InsecureSkipVerify: true,
 }

 c, err := tls.Dial("tcp", host+":443", tcfg)
 if err != nil {
  log.Fatal(err)
 }
 defer c.Close()

 c.Write([]byte(http2.ClientPreface))
 f := http2.NewFramer(c, c)
 if err := f.WriteSettings(); err != nil {
  log.Fatal(err)
 }
 if err := f.WriteWindowUpdate(0, 1<<30); err != nil {
  log.Fatal(err)
 }

 go func() {
  for {
   frame, err := f.ReadFrame()
   if err != nil {
    log.Fatal(err)
   }

   switch f := frame.(type) {
   case *http2.SettingsFrame:
    f.ForeachSetting(func(s http2.Setting) error {
     log.Println(s)
     return nil
    })
   default:
    log.Println(f)
   }
  }
 }()

 go func() {
  for {
   time.Sleep(1 * time.Second)
   u := time.Now().Unix()
   // me is lazy lol
   s := *(*[8]byte)(unsafe.Pointer(&u))
   log.Println(s)
   if err := f.WritePing(false, s); err != nil {
    log.Fatal(err)
   }
  }
 }()

 select {}
}
