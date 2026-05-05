# Name: David Manuana
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
    def __init__(self, size, hash_type):
        self.size = size
        self.hash_type = hash_type
        self.table = [None] * size
        self.collisions = 0
        self.items = 0

    # choose hash function
    def hash_function(self, key):
        if self.hash_type == 1:
            return len(key) % self.size

        if self.hash_type == 2:
            total = 0
            i = 0
            for ch in key:
                total += ord(ch) * (i + 1)
                i += 1
            return total % self.size

        total = 0
        for ch in key:
            total = (total * 31 + ord(ch)) % self.size
        return total

    # add item, do not overwrite duplicates
    def add(self, key, data):
        index = self.hash_function(key)
        new_node = Node(key, data)

        if self.table[index] == None:
            self.table[index] = new_node
            self.items += 1
            return

        cur = self.table[index]

        while cur.next != None:
            self.collisions += 1
            cur = cur.next

        self.collisions += 1
        cur.next = new_node
        self.items += 1

    # search for first matching key
    def search(self, key):
        index = self.hash_function(key)
        cur = self.table[index]

        while cur != None:
            if cur.key == key:
                return cur.data
            cur = cur.next

        return None

    # count empty buckets
    def wasted_space(self):
        count = 0

        for bucket in self.table:
            if bucket == None:
                count += 1

        return count


class LinearHashTable:
    # linear probing
    def __init__(self, size, hash_type):
        self.size = size
        self.hash_type = hash_type
        self.table = [None] * size
        self.collisions = 0
        self.items = 0

    # choose hash function
    def hash_function(self, key):
        if self.hash_type == 3:
            if key == "":
                return 0
            return (ord(key[0]) + len(key)) % self.size

        if self.hash_type == 4:
            total = 0
            i = 0
            for ch in key:
                total += ord(ch) * (i + 3)
                i += 1
            return total % self.size

        total = 5381
        for ch in key:
            total = ((total * 33) + ord(ch)) % self.size
        return total

    # add item, do not overwrite duplicates
    def add(self, key, data):
        index = self.hash_function(key)
        start = index

        while self.table[index] != None:
            self.collisions += 1
            index = (index + 1) % self.size

            if index == start:
                return

        self.table[index] = (key, data)
        self.items += 1

    # search for first matching key
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

    # count empty slots
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


def run_attempt(attempt_name, table_kind, size, hash_type, movies):
    print("==============================")
    print(attempt_name)
    print("==============================")
    print()

    if table_kind == "linked":
        title_table = LinkedHashTable(size, hash_type)
        quote_table = LinkedHashTable(size, hash_type)
        method = "Linked List"
    else:
        title_table = LinearHashTable(size, hash_type)
        quote_table = LinearHashTable(size, hash_type)
        method = "Linear Probing"

    title_time = build_table(title_table, movies, True)
    quote_time = build_table(quote_table, movies, False)

    print_stats("Hash Table 1: Movie Title as Key", method, title_table, title_time)
    print_stats("Hash Table 2: Movie Quote as Key", method, quote_table, quote_time)


def main():
    movies = load_movies("MOCK_DATA.csv")

    print("Total movie records loaded:", len(movies))
    print()

    run_attempt(
        "ATTEMPT 1 - LINKED LIST / POOR HASH",
        "linked",
        1009,
        1,
        movies
    )

    run_attempt(
        "ATTEMPT 2 - LINKED LIST / BETTER HASH",
        "linked",
        2003,
        2,
        movies
    )

    run_attempt(
        "ATTEMPT 3 - LINEAR PROBING / POOR HASH",
        "linear",
        20011,
        3,
        movies
    )

    run_attempt(
        "ATTEMPT 4 - LINEAR PROBING / BETTER HASH",
        "linear",
        20011,
        4,
        movies
    )

    run_attempt(
        "ATTEMPT 5 - LINEAR PROBING / ROLLING HASH",
        "linear",
        17011,
        5,
        movies
    )


if __name__ == "__main__":
    main()