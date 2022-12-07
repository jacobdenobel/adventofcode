use std::{fs::File, io::Read};
use std::str::Split;

fn read_data(i: i32) -> String {
    let mut content = String::new();
    let mut file = File::open(format!("data/{}", i))
        .expect("file not found");
    file.read_to_string(&mut content)
        .expect("Stork");
    
    return content;
}

fn main() {
    let content = read_data(1);
    let things: Split<&str> = content.split(", ");
    
    let mut x: i32 = 0;
    let mut y: i32 = 0;
    let mut d: i32 = 1;

    for thing in things {
        let mut chars = thing.chars();
        let dir = chars.nth(0).unwrap();    
        let n: i32 = chars.map(|c| c.to_digit(10).unwrap()).sum::<u32>().try_into().unwrap();    
        if dir == 'L' {
            d -= 1;
        } else {
            d += 1;
        }
        if d < 0 {
            d = 3;
        }

        if d > 3 {
            d = 0;
        }
        
        match d {
            0 => x= x-n,
            1 => y= y+n,
            2 => x= x+n,
            3 => y= y-n,
            _ => println!("kanker")
        } 
        println!("{}: ({}, {}) {}", thing, x, y, n);
    }
    println!("{}", x.abs() + y.abs());

}
