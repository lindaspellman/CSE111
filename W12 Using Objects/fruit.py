def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")

    # List reverse
    fruit_list.reverse()

    # Updated list
    print(f"Reversed list: {fruit_list}")

    # Append "orange" to end of fruit_list
    fruit_list.append("orange")
    print(f"Append orange: {fruit_list}")

    # Find "apple" and insert "cherry" before "apple"
    apple = fruit_list.index("apple")
    fruit_list.insert(apple, "cherry")
    print(f"Insert cherry: {fruit_list}")

    fruit_list.remove("banana")
    print(f"Banana removed: {fruit_list}")

    popped = fruit_list.pop()
    print(f"Popped: {popped} {fruit_list}")

    fruit_list.sort()
    print(f"Sorted list: {fruit_list}")

    fruit_list.clear()
    print(f"Cleared list: {fruit_list}")

main()
