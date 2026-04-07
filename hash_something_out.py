# Name: David
# Course: COS 226
# Assignment: Hash something out
# Purpose: Build two hash tables for movie records and test different hash functions.
# Date: 04/06/2026

import time
import csv


class MovieRecord:
    # store one movie row
    def __init__(self, title, quote):
        self.title = title
        self.quote = quote

    def __str__(self):
        return self.title + " | " + self.quote


class Node:
    # linked list node
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.next = None


class LinkedHashTable:
    # linked list chaining
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
        self.collisions = 0
        self.items = 0

    # ATTEMPT 1 HASH
    def hash_function(self, key):
        return len(key) % self.size

    def add(self, key, data):
        index = self.hash_function(key)
        new_node = Node(key, data)

        if self.table[index] == None:
            self.table[index] = new_node
            self.items += 1
            return

        cur = self.table[index]
        while cur != None:
            self.collisions += 1
            if cur.key == key:
                cur.data = data
                return
            if cur.next == None:
                break
            cur = cur.next

        cur.next = new_node
        self.items += 1

    def search(self, key):
        index = self.hash_function(key)
        cur = self.table[index]

        while cur != None:
            if cur.key == key:
                return cur.data
            cur = cur.next
        return None

    def wasted_space(self):
        count = 0
        for bucket in self.table:
            if bucket == None:
                count += 1
        return count


class LinearHashTable:
    # linear probing
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
        self.collisions = 0
        self.items = 0

    # ATTEMPT 3/4/5 HASH
    def hash_function(self, key):
        if key == "":
            return 0
        return (ord(key[0]) + len(key)) % self.size

    def add(self, key, data):
        index = self.hash_function(key)
        start = index

        while self.table[index] != None:
            self.collisions += 1
            if self.table[index][0] == key:
                self.table[index] = (key, data)
                return
            index = (index + 1) % self.size
            if index == start:
                return

        self.table[index] = (key, data)
        self.items += 1

    def search(self, key):
        index = self.hash_function(key)
        start = index

        while self.table[index] != None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size
            if index == start:
                break
        return None

    def wasted_space(self):
        count = 0
        for slot in self.table:
            if slot == None:
                count += 1
        return count

def load_movies(filename):
    movies = []

    f = open(filename, "r", encoding="utf-8")
    reader = csv.DictReader(f)

    for row in reader:
        title = row["movie_title"].strip()
        quote = row["quote"].strip()

        if title == "" or quote == "":
            continue

        movies.append(MovieRecord(title, quote))

    f.close()
    return movies

def build_table(table, movies, use_title):
    start = time.time()

    for movie in movies:
        if use_title:
            key = movie.title
        else:
            key = movie.quote
        table.add(key, movie)

    end = time.time()
    return end - start

def print_stats(name, method_name, table, build_time):
    print(name)
    print("Method:", method_name)
    print("Items:", table.items)
    print("Table size:", table.size)
    print("Wasted space:", table.wasted_space())
    print("Collisions:", table.collisions)
    print("Construction time:", build_time)
    print()

def main():
    movies = load_movies("MOCK_DATA.csv")

    print("Total movie records loaded:", len(movies))
    print()

 # ATTEMPT 1
    title_table = LinkedHashTable(1009)
    quote_table = LinkedHashTable(1009)

    t1 = build_table(title_table, movies, True)
    t2 = build_table(quote_table, movies, False)

    print("ATTEMPT 1 - LINKED LIST / POOR HASH")
    print()
    print_stats("Hash Table 1: Movie Title as Key", "Linked List", title_table, t1)
    print_stats("Hash Table 2: Movie Quote as Key", "Linked List", quote_table, t2)


if __name__ == "__main__":
    main()