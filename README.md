# ⏰ Object Reference in Python (Time Class)

## 📌 Description

This Python program demonstrates the concept of **object reference**. Instead of creating a new object, one variable refers to the same object in memory.

---

## 🚀 Features

* Defines a `Time` class
* Creates an object with time values
* Demonstrates reference copy (`t2 = t1`)
* Shows that both variables point to the same object

---

## 🛠️ How It Works

1. A class `Time` is created with:

   * `hrs`, `min`, `sec` as attributes

2. An object `t1` is created with values `(10, 25, 45)`.

3. Another variable `t2` is assigned:

   ```python
   t2 = t1
   ```

   👉 This does NOT create a new object
   👉 Both `t1` and `t2` point to the SAME object in memory

4. When `display()` is called:

   * Both `t1` and `t2` print the same values

---

## 💻 Code

```python
class Time:
    def __init__(self, hrs=0, min=0, sec=0):
        self.hrs = hrs
        self.min = min
        self.sec = sec

    def display(self):
        print(f"{self.hrs:02d} : {self.min:02d} : {self.sec:02d}")


# Main program
t1 = Time(10, 25, 45)
t1.display()

t2 = t1   # reference copy (same object)
t2.display()
```

---

## ▶️ Example Output

```
10 : 25 : 45
10 : 25 : 45
```

---

## 🧠 Important Concept

* `t1` and `t2` are **not separate objects**
* They are **two references to the same object**

👉 If you modify one, the other also changes:

```python
t2.hrs = 99
t1.display()   # Output will also change!
```

---

## 📚 Concepts Used

* Class and Object
* Object reference
* Memory sharing

---

## 🎯 Use Case

This helps you understand:

* Difference between **copy** and **reference**
* Very important for debugging and interviews

---

## ⚠️ Common Mistake

Many beginners think:

```
t2 = t1   ❌ makes a copy
```

But actually:

```
t2 = t1   ✅ creates a reference
```

---

## 🔧 Future Improvements

* Use `copy()` or `deepcopy()` for actual copying
* Demonstrate difference between shallow and deep copy

---

## 📄 License

This project is open-source and free to use.

<img width="764" height="681" alt="image" src="https://github.com/user-attachments/assets/bc2b3b2d-f1ea-4638-a0a8-0419a9642aa6" />

