```python
def add(*args):
    for n in args:
        print(n)
```

### Tkinter Layout Managers
```plain text
If you don't specify one of these your layout/button wont show on screen

pack()          # Always starts at the top and places others below
place()         # All about precise placement provide x and y value
grid()          # Uses columns and rows to specify placement

grid is preferable 
cant mix grid and pack
```