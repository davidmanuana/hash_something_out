# Hash something out

## Attempt 1
I used a linked list hash table with a poor hash function based only on the length of the key.

### Why I tried it
I wanted a simple starting point to compare against later attempts.

### Results
- Title table wasted space: 
- Title table collisions: 
- Title table construction time: 
- Quote table wasted space: 
- Quote table collisions: 
- Quote table construction time: 

### Reflection
This method caused many collisions because many strings had similar lengths.

## Attempt 2
I used a linked list hash table with a weighted character hash function.

### Why I tried it
I wanted a better spread of keys across the table.

### Results
- Title table wasted space: 
- Title table collisions: 
- Title table construction time: 
- Quote table wasted space: 
- Quote table collisions: 
- Quote table construction time: 

### Reflection
This worked better than attempt 1 because it used more information from the string.

## Attempt 3
I used linear probing with a weak hash function based on first character and length.

### Why I tried it
I wanted a linear probing version with a poor hash to compare against chaining.

### Results
- Title table wasted space: 
- Title table collisions: 
- Title table construction time: 
- Quote table wasted space: 
- Quote table collisions: 
- Quote table construction time: 

### Reflection
This caused clustering and many collisions.

## Attempt 4
I used linear probing with a weighted character hash.

### Why I tried it
I wanted to improve linear probing by using a better hash.

### Results
- Title table wasted space: 
- Title table collisions: 
- Title table construction time: 
- Quote table wasted space: 
- Quote table collisions: 
- Quote table construction time: 

### Reflection
This improved the spread and lowered collisions.

## Attempt 5
I used linear probing with a rolling hash and a different table size.

### Why I tried it
I wanted to optimize the best earlier method even more.

### Results
- Title table wasted space: 
- Title table collisions: 
- Title table construction time: 
- Quote table wasted space: 
- Quote table collisions: 
- Quote table construction time: 

### Reflection
This was my final optimization attempt and I compared it to the earlier four.

## Final Reflection
The linked list methods handled collisions better when the hash was weak, but they used more bucket chaining. Linear probing needed a much better hash function to avoid clustering. The better hash functions performed much better than the weak ones. My best overall attempt was the one that had the best balance between low collisions, reasonable construction time, and acceptable wasted space.