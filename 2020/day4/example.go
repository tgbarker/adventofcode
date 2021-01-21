package main

import (
    "bufio"
    "fmt"
    "log"
    "os"
    "strings"    
    "strconv"
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

var eyecolors = "amb blu brn gry grn hzl oth"

func (p *Passport) isValid() bool {
    return len(p.byr) > 0 && len(p.iyr)  > 0 && len(p.eyr)  > 0 && len(p.hgt)  > 0 && len(p.hcl)  > 0 && len(p.ecl)  > 0 && len(p.pid)  > 0
} 

func (p *Passport) isValidPt2() bool {
 if (!p.isValid()){
         return false;
     } else {
        var byr, eByr = strconv.Atoi(p.byr)
        if eByr != nil || (byr < 1920 || byr > 2002 ){
            fmt.Printf("Failed byr - %v\n", byr)
            return false
        }
        var iyr, eIyr = strconv.Atoi(p.iyr)
        if eIyr != nil || (iyr < 2010 || iyr > 2020 ){
            fmt.Printf("Failed iyr - %v\n", byr)
            return false
        }
        var eyr, eEyr = strconv.Atoi(p.eyr)
        if eEyr != nil || (eyr < 2020 || eyr > 2030 ){
            fmt.Printf("Failed eyr - %v\n", byr)
            return false
        }

		if !strings.Contains(eyecolors, p.ecl) {
            fmt.Printf("Failed ecl - %v\n", p.ecl)
			return false
        }

        if len(p.hgt) > 2 {
            hgt := p.hgt[:len(p.hgt)-2]
            fmt.Printf("Checking hgt - %v %v\n", hgt, p.hgt)
            if strings.HasSuffix(p.hgt, "cm") {
                if (hgt < "150" || hgt > "193") {
                fmt.Printf("Failed hgt cm - %v\n", p.hgt)
                return false
                }
            } else if strings.HasSuffix(p.hgt, "in") { if (hgt < "59" || hgt > "76") {
                fmt.Printf("Failed hgt in - %v\n", p.hgt)
                return false
            }
            } else {
                fmt.Printf("Failed hgt format - %v\n", p.hgt)
                return false
            }
        } else {
            return false 
        }
        
        if len(p.hcl) == 7 && p.hcl[0]== '#' {
            for i := 0 ; i < len(p.hcl); i++ {
                character := p.hcl[i]
                valid := (character >= '0' || character <= '9') || (character >= 'a' || character <= 'f')
                if !valid {
                    fmt.Printf("Failed hcl - %v\n", p.hcl)
                    return false;
                }
            }
        } else {
            return false;
        }

        if len(p.pid) == 9 {
            for i := 0 ; i < len(p.pid); i++ {
                character := p.pid[i]
                valid := (character >= '0' || character <= '9')
                if !valid {
                    fmt.Printf("Failed pid - %v\n", p.pid)
                    return false;
                }
            }
        } else {
            return false
        }
        return true
    }
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
    var validPassportsPt2 int

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
            // fmt.Printf("PP parsed : '%v'\n", *pp)   
            // fmt.Printf("PP parsed 1 : '%v'\n", pp.isValid())   
            // fmt.Printf("PP parsed 2 : '%v'\n", pp.isValidPt2())   
            if(pp.isValid()){
                validPassports++
            }
            if(pp.isValidPt2()){
                validPassportsPt2++
            }
        }
    }
    fmt.Println("Nb Valid Passports : ", validPassports , validPassportsPt2)
}
