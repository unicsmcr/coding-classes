# Extensions

### Recursion <a id="Recursion"></a>

Recursion is a fun and occasionally useful concept. It refers to the ability to have functions **call themselves**

```text
# A recursive function calls itself

# This function will count down to zero
def count_down(number):
    print(number)
    if (number > 0): # Stop recursing once we've reached 0
        count_down(number - 1) # "Recursive" call!
    
count_down(3) # Will print 3 2 1 0
```

