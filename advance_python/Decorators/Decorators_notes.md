# Decorators in Python

> Python Blog [Dan Blog](https://dbader.org/blog/python-decorators).
> To understand decorators requires a solid grasp of several advanced concepts in the language—including the [properties of first-class functions](https://dbader.org/blog/python-first-class-functions).

Any sufficiently generic functionality you can “tack on” to an existing class or function’s behavior makes a great use case for decoration. This includes:

- logging,
- enforcing access control and authentication,
- instrumentation and timing functions,
- rate-limiting,
- caching; and more.

## Python Decorator Basics

Now, what are decorators really? They “decorate” or “wrap” another function and let you execute code before and after the wrapped function runs.

Decorators allow you to define reusable building blocks that can change or extend the behavior of other functions. And they let you do that without permanently modifying the wrapped function itself. The function’s behavior changes only when it’s decorated.

Now what does the implementation of a simple decorator look like? In basic terms, a decorator is a callable that takes a callable as input and returns another callable.

```python
def null_decorator(func):
    return func
```
As you can see, null_decorator is a callable (it’s a function), it takes another callable as its input, and it returns the same input callable without modifying it.

Let’s use it to decorate (or wrap) another function:

```python
def greet():
    return 'Hello'

greet = null_decorator(greet)

>>> greet()
Hello
```
In this example I’ve defined a greet function and then immediately decorated it by running it through the null_decorator function. I know this doesn’t look very useful yet (I mean we specifically designed the null decorator to be useless, right?) but in a moment it’ll clarify how Python’s decorator syntax works.

Instead of explicitly calling null_decorator on greet and then reassigning the greet variable, you can use Python’s @ syntax for decorating a function in one step:

```python
@null_decorator
def greet():
    return 'Hello!'

>>> greet()
Hello!
```

```python
def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper

@uppercase
def greet():
    return 'hello!'

>>> greet()
HELLO!
```
Unlike null_decorator, our uppercase decorator returns a different function object when it decorates a function:

```python
>>> greet
<function greet at 0x10e9f0950>

>>> null_decorator(greet)
<function greet at 0x10e9f0950>

>>> uppercase(greet)
<function uppercase.<locals>.wrapper at 0x10da02f28>
```

## Applying Multiple Decorators to a Single Function

Perhaps not surprisingly, you can apply more than one decorator to a function. This accumulates their effects and it’s what makes decorators so helpful as reusable building blocks.

Here’s an example. The following two decorators wrap the output string of the decorated function in HTML tags. By looking at how the tags are nested you can see which order Python uses to apply multiple decorators:

```python
def strong(func):
    def wrapper():
        return '<strong>'+func+'</strong>'
    return wrapper

def emphasis(func):
    def wrapper():
        return '<em>'+func+'</em>'
    return wrapper

@strong
@emphasis
def greet():
    return 'Hello!'

>>> greet()
'<strong><em>Hello!</em></strong>'
```
This clearly shows in what order the decorators were applied: from bottom to top. First, the input function was wrapped by the @emphasis decorator, and then the resulting (decorated) function got wrapped again by the @strong decorator.

To help me remember this bottom to top order I like to call this behavior decorator stacking. You start building the stack at the bottom and then keep adding new blocks on top to work your way upwards.

## Decorating Functions That Accept Arguments

All examples so far only decorated a simple nullary greet function that didn’t take any arguments whatsoever. So the decorators you saw here up until now didn’t have to deal with forwarding arguments to the input function.

If you try to apply one of these decorators to a function that takes arguments it will not work correctly. How do you decorate a function that takes arbitrary arguments?

This is where Python’s [*args and **kwargs feature](https://www.youtube.com/watch?v=WcTXxX3vYgY) for dealing with variable numbers of arguments comes in handy. The following proxy decorator takes advantage of that:


