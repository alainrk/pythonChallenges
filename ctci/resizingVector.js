/*
Implement a vector (mutable array with automatic resizing):

New raw data array with allocated memory can allocate int array under the hood, just not use its features start with 16, or if starting number is greater, use power of 2 - 16, 32, 64, 128
- size() - number of items
- capacity() - number of items it can hold
- is_empty()
- at(index) - returns item at given index, blows up if index out of bounds
- push(item)
- insert(index, item) - inserts item at index, shifts that index's value and trailing elements to the right
- prepend(item) - can use insert above at index 0
- pop() - remove from end, return value
- delete(index) - delete item at index, shifting all trailing elements left
- remove(item) - looks for value and removes index holding it (even if in multiple places)
- find(item) - looks for value and returns first index with that value, -1 if not found
- resize(new_capacity) // private function
when you reach capacity, resize to double the size
when popping an item, if size is 1/4 of capacity, resize to half

Time
- O(1) to add/remove at end (amortized for allocations for more space), index, or update
- O(n) to insert/remove elsewhere

Space
- contiguous in memory, so proximity helps performance
- space needed = (array capacity, which is >= n) * size of item, but even if 2n, still O(n)
*/

/**
 * @private
 * @param {number} size
 * @returns {number} power of 2 containing amount, minimum capacity is 16
 */
function calcCapacity (size) {
  return Math.pow(2, Math.max(4, Math.ceil(Math.log2(size))))
}

class Vector {
  constructor (...items) {
    this.__size = items.length
    this.__cap = calcCapacity(this.__size)
    this.vector = new Array(this.__cap)
    for (let i = 0; i < this.__size; i++) {
      this.vector[i] = items[i]
    }
  }

  size () {
    return this.__size
  }

  cap () {
    return this.__cap
  }

  isEmpty () {
    return this.__size === 0
  }

  increaseCapacity (newSize) {
    const newCapacity = calcCapacity(newSize)
    if (newCapacity > this.__cap) {
      this.__cap = newCapacity
      const newVector = new Array(newCapacity)
      for (let i = 0; i < this.__size; i++) {
        newVector[i] = this.vector[i]
      }
      this.vector = newVector
    }
  }

  at (index) {
    if (index > this.__size - 1) {
      throw new Error('Vector: index out of bound')
    }
    return this.vector[index]
  }

  push (item) {
    this.increaseCapacity(this.__size + 1)
    this.vector[this.__size] = item
    this.__size++
  }
}

const v = new Vector(1, 2, 3)
for (let i = 4; i < 35; i++) {
  v.push(i)
  console.log(`Cap = ${v.cap()}, size = ${v.size()}, Vec = ${v.vector}`)
}
// const assert = require('assert')
// assert.deepStrictEqual(calcCapacity(1), 16)
// assert.deepStrictEqual(calcCapacity(2), 16)
// assert.deepStrictEqual(calcCapacity(9), 16)
// assert.deepStrictEqual(calcCapacity(16), 16)
// assert.deepStrictEqual(calcCapacity(17), 32)
// assert.deepStrictEqual(calcCapacity(64), 64)
// assert.deepStrictEqual(calcCapacity(65), 128)
// assert.deepStrictEqual(calcCapacity(1023), 1024)
// assert.deepStrictEqual(calcCapacity(1024), 1024)
// assert.deepStrictEqual(calcCapacity(1025), 2048)