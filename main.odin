package main

import "core:mem"
import "core:fmt"
main :: proc() {
    fmt.println(size_of(map[int]int));
    fmt.println(size_of(mem.Allocator));
}
