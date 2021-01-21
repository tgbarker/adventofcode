package main

import (
    "bufio"
    "fmt"
    "log"
    "os"
    "strings"
)

type Passport struct {
    byr string //(Birth Year)
    iyr string //(Issue Year)
    eyr string //(Expiration Year)
    hgt string //(Height)
    hcl string //(Hair Color)
    ecl string //(Eye Color)
    pid string //(Passport ID)
    cid string //(Country ID)
}

func (p *Passport) isValid() bool {
    return len(p.byr) > 0 && len(p.iyr)  > 0 && len(p.eyr)  > 0 && len(p.hgt)  > 0 && len(p.hcl)  > 0 && len(p.ecl)  > 0 && len(p.pid)  > 0
} 

func createPassport(m map[string]string) *Passport {
    return &Passport {
        byr : m["byr"],
        iyr : m["iyr"],    
        eyr : m["eyr"],    
        hgt : m["hgt"],    
        hcl : m["hcl"],    
        ecl : m["ecl"],    
        pid : m["pid"],    
        cid : m["cid"],    
    }
}
	
func main() {

    inputFile := os.Args[1]
    
    file, err := os.Open(string(inputFile))
    if err != nil {
        log.Fatal(err)
    }
    defer file.Close()

    scanner := bufio.NewScanner(file)
    var ppLine string
    var validPassports int

    for scanner.Scan() {
        line := scanner.Text()
        if(len(line) > 0){
            ppLine += line + " "
        } else {
            ppLine = strings.Trim(ppLine, " ")
            fmt.Printf("Doc line : '%v'\n", ppLine)     
            var m map[string]string
            var ss []string
            ss = strings.Split(ppLine, " ")
            m = make(map[string]string)
            for _, pair := range ss {
                z := strings.Split(pair, ":")
                m[z[0]] = z[1]   
            }
            ppLine = ""
            pp := createPassport(m)
            fmt.Printf("PP parsed : '%v'\n", *pp)   
            fmt.Printf("PP parsed : '%v'\n", pp.isValid())   
            if(pp.isValid()){
                validPassports++
            }
        }
    }
    fmt.Println("Nb Valid Passports : ", validPassports)
}
