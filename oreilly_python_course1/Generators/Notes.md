One of Python's most useful features is the for statement, which is used to iterate over data. 
As you may have noticed, the for statement works with a wide-variety of objects, such as lists, dictionaries, 
sets, and files. It's also used in a variety of related features, such as list comprehensions.
One of the most powerful features of iteration is that it can be easily customized. 
So in this lesson, we look at the iteration protocol and how to customize it using generator functions. 
I also show how to apply iteration to data processing pipelines, a particularly powerful technique for working
with data and problems involving workflows.


### Video 2
Let's start by talking about the basics of how the for-loop works in Python, or how iteration works. 
As you know, if you have an object like a list or something, let's say you have a list of stock names, for instance, 
you can do a for-loop to iterate over the data, that can say, for name in names: print(name). U
nderneath the covers of that, there's a very specific protocol that is being carried out. What is happening is that 
Python goes to names and it asks it for an iterator. There's a special method, iterer, that is executed 
to do this, and you'll get back an iterator object. Once you have that, what happens is, Python will repeatedly 
call next on it to pull items out. Then this happens until you get a StopIteration exception. This is the low-level 
machinery that is being used by the for-loop. In fact, anyplace that you use the for-loop, this is actually 
happening behind the scenes. For example, if you open up a file and then you do a for-loop on a file, 
what's actually happening is, Python goes to the file and says, "Give me an iterator," which happens to be the file 
itself, in this case. Then you call next on it and you'll start getting lines of the file coming out. 
That will continue until you get to the end of the file and you get a StopIteration. 
Everything that plugs into the for-loop does follow this convention, and if you're inclined, you can certainly make 
your own objects plug into the for-loop. You can make a class that has an iter method, and you implement next, 
and so forth. I'm not going to do that, however, because there is actually an easier way to customize iteration. 
Let's say you did wanna customize the for-loop for some reason. One of the ways that you can do that, is you can 
define something known as a generator function. To illustrate, I'm gonna make a really simple example just to 
start, like countdown(n). What I'm gonna here is, I'll make a function. I'll just say, ('Counting from', n). 
Then I'm going to make a while-loop that carries out the count, but I'm gonna use a new statement that we have not 
seen before, which is the yield statement. What is going on here is, this is going to emit a value, and then 
I'm gonna decrement the loop. I'll put a ('Done') at the end. What happens with this function, is this is 
something that feeds the for-loop. Like if I were to say, for x in countdown(5), print (x), what you're going to see, 
is this countdown function feeding values to the for-loop, so you see the printing message taking place, you see the 
five down to one, and then you see the Done message. Under the covers, how this works, is that you call the function. 
Turns out that nothing happens. This is very odd, by the way, but you call the function, you don't see any output, 
but you get this generator object as a result. What this generator object is, is it's kind of that function in a 
suspended execution state, and it's not going to start running until you start iterating on it. The first step of 
iteration is that you go ahead and you create an iterator. Again, nothing happens. In fact, it comes back saying, 
"Well, here's the generator object." The function will not start running until next gets called on it. 
When you call next, all the sudden, you see the function wake up. It's like, 
"Oh, I'm counting down from five," and then five pops out. What has happened at this point, 
is that the function has suspended itself on that yield. It popped out a value, but now the function 
is just sitting there. It's waiting for you to wake it up again. It's not going to wake up until you 
call next on it. If you call next on it, it will cycle back around, decrement the value, and split it out. 
Now what is happening is that while-loop is sort of emitting values, and then when the function is done, you get a 
StopIteration. A very convenient way to customize iteration is to define a generator like that. Doing something 
like a countdown may be not the most compelling thing, but you can write all sorts of little utilities for 
yourself based on this. For example, one of the Unix tools that I use a fair amount, is something like the grep 
command. This is something that lets you search a file, like you could say, grep IBM in data/portfolio.csv, and 
it lets you find matching lines. I could do something like that in Python. I could say, hey, let's do a grep for 
some pattern in a file name, give me a file name, and then what I could do is, open up a file. I could say, with 
open(filename) as f, for line in f, if the pattern is in the line, yield the line. Wow, a lot of indentation on that. 
This would become a function that I could use. I could say, for line in grep 'IBM', 'Data/portfolio.cvs'), 
print(line) and I've just done the same thing that that Unix tool uses. Customizing iteration, it's a very 
cool thing to be able to do that. Generators are one way to kind of plug into that with the for-loop. Turns out 
there's another way to define a generator, that is useful to know about. One of the features that we 
talked about earlier, was this idea of a list comprehension. Like if you had a list, you could say, 
squares is equal to x times x for x in nums, for instance, and it would generate a new list for you. 
Turns out that there's a variant of this that uses generator. If you change the square brackets to parentheses, 
you will get a generator object that will produce the same result if you do a for-loop on it. If I say, for x in 
squares, for instance, and print it out, you will see it produce the same kind of output, it's producing squares. 
This is something that is sometimes useful if you don't care about actually creating that temporary list. For 
instance, if I say, squares is equal to x times x for x in nums, it actually makes a fully populated list as a 
result, and if I were ever to pass that into a function or something, maybe I don't care about the list anymore, 
turns out that it's actually a little bit more efficient to use a generator instead, because it doesn't actually 
create a list, it just creates an iterator, and then you can sum it up, and then you sort of throw it away. You 
could even just do it in the sum function itself. One little bit note about Python syntax, is if you ever see that 
convention here with a generator, you can eliminate one of the parentheses, kind of simplify it down. This is 
another way of defining generators, to write one of these generator expressions. We might be able to replace 
something like this grep with one of those, by the way. I mean, one of the things you could do is, you could say, 
let's open up a file, for instance, and then I could say, IBM is equal to line for line in f if 'IBM' is in the line. 
Then if you did a for-loop on that, then you would get the same effect. These are some ways you can customize 
iteration, with either a generator function or one of these generator expression. Now, one thing I do have 
to warn you about, generators are a one-time use. If you've made like a countdown, for instance, and then I said, 
for x in c, turns out that I can only do that once. If I try to do a for-loop on it again, it doesn't run again. 
A generator lets you iterate once, then it's done. If I want to redo the for-loop, I would have to re-create 
the countdown from scratch, and do it again. If that is a concern, like you wanna be able to repeatedly do 
iteration, there is a way to do that using classes that I think is worth knowing about. Let's say you wanted 
to be able to iterate repeatedly. One of the ways to do that, is you could make an object that maybe represents 
like a countdown. You could say, okay, here's the start of the countdown. Then what you can do, is define the 
iterer method actually as a generator, so what you could do is, you write iterer that carries out the count 
using yield. Okay, this is the same code as before, just something like that. Turns out that that will create 
something that you can just repeatedly do a for-loop on. That's also a useful trick to know about, is if you do 
need something where you just constantly need to iterate, you can make iter itself use this yield statement, 
and you just use it to drive the iteration process. In the next couple parts, I'm gonna talk about some practical 
applications of using generators that's it's actually a really powerful feature of the language, 
especially for data-processing tasks.


### video 3
- So one of the things that I have to do, fairly often, is watch real time data sources. For instance, like a log 
- file on a server. And what I'm gonna do here is talk about how to use a generator function to monitor that data in 
- Python. To start this off, one of the ways that I often will watch a log file on for instance a web server or 
- something like that is to the Unix tail minus f command. Many people have seen this before but what you can do 
- is point at maybe a log file and then watch as data is being being written to it. What I've got here is actually 
- I have a log file that is watching stock market data. So you'll slowly see it being updated in the bottom there. 
- You sort of see price updates and information being written. So what I'm gonna do is talk about how to write Python 
- code that watches this log file. And so I'm gonna make a file, follow.py, and what we're gonna do is watch a 
- log file, stocks in this case here. And here's how I'm gonna do this. There's a few things about files that 
- might be a little bit unusual here, but what I'm gonna do is I'm gonna open up a file. Gonna open up 
- this stocklog.csv file for reading, and then I'm gonna seek to the end of the file. This is maybe the 
- unusual part, it's like okay I'm gonna go to the end of the file and then I'm gonna write a loop where 
- I just constantly try to read lines at the end of the file. Okay, so we're gonna read a new line of data, 
- and then if there's nothing there, like we don't get any data, what I'm gonna do is essentially sleep briefly 
- and then try again. This is kinda like a retry sort of thing. I'm gonna write a file that kinda reads at the 
- end of the file, does a retry, and then maybe just to start I'll print out the line here. Okay, so let's 
- print out the line. Actually, I'll put a Got line so we can see that. I'm gonna try to run that, and just 
- see whether it looks at all similar to this Unix tail minus F that I just did. Let's go ahead and run that 
- for a second. Okay, so I have this program kind of watching the end of the file. If it's working correctly, 
- I should see it start to print lines as they come in here. Might take a second for data to update. So there 
- a I got a line that said, "Cat". Okay, so the thing is kind of watching the end of the file. Now one of the
- things that you might do is try to do some processing on the data, after you've read it. Maybe instead of 
- just printing out the lines, maybe I'll split the data up. Maybe I'll split on a Cava, and then maybe I 
- would look at some of the data. I happen to know that like the change in the stock price, I think is in 
- like row 4. So maybe I could watch the file. I could say, well okay, I'm gonna watch the file and then if 
- like the change in the price is less than zero maybe I would pull out some additional information. Like 
- name is equal to row zero, the price is equal to row one, print, let's print some of these things formatted 
- out maybe. Okay, so what I got here is we're kinda taking this programming maybe extended it a little 
- bit more. What I've got is I'm watching a file, but then I'm watching the file for events. Basically 
- negative change and price. I'm trying to figure out what stocks are falling in price. Let's run it 
- just to kinda see if it's gonna work here. So if it's working, what it should do is it should start 
- printing out a table showing me stocks that are down in price. Okay, so it's telling me Microsoft is 
- down, a few others are down, and so forth. Again think about watching maybe like a web server log and 
- you're looking for anomalous events, or something like that. This kind of code, this is a perfect place 
- to use something like a generator function. Turns out that this act of following the file is something 
- that I could package up into a function. Like I could say follow some file name, and I could take whole 
- first part of the code and sort of package it up into one of these generators. I could say okay well the 
- way that you follow a file is you open it, you do this little while loop, and then when you get a line you 
- emit it with the yield statement. Okay, so we're going to emit basically a line doing that. This code down a
- t the bottom can be recast as a for loop. I could say for line and follow, you know, stocklog.csv, and the
- code will actually work exactly the same as it's working now. Let's run it and see if it does that. So 
- is happening now, is I've got this one little function that's just sitting there constantly monitoring the 
- file, and it's using Yield to kinds spin out lines, and then this code down below is sort of watching that f
- eed, if you will, and looking for events to take place. These negative stock change events. Very kind of 
- interesting clever thing that is taking place there. One of the things that's really kind of amazing about 
- this is that this generator function that I wrote here is extremely general purpose. I could use that to watch 
- a web server log. I could use it to watch stocks. There's nothing about this function that has anything 
- whatsoever to do with the contents of the data. It's just reading lines off. That is a very powerful idea 
- that I could take iteration and just package it up into a little self contained unit like that. So that's 
- one of the powers of generators is being able to do that. The code down here at the bottom, in some sense, 
- is also a more powerful than it was before. This for line, in follow, is actually a more general idea of 
- just doing a for loop. There's nothing about this code that has anything to do with following a file. For 
- instance, if I didn't wanna follow the file, and maybe I could just open the file. In that code at the 
- bottom would work fine. If I were to do that, what it would do is sort of like a quick post processing 
- thing. Like if I run it, it would just process the entire file and then quit. It doesn't even have to 
- pull anything from a file. I mean you could get the lines from somewhere else. Maybe you opened up a 
- file, like you said, open up, you know, datastocklog.csv, and then you said lines is equal to f read lines,
- and then you did an a for loop on lines. That would work just fine as well. The whole idea is that this for 
- loop at the bottom doesn't really care what the thing is that you're iterating on. There's a lot of flexibility 
- there. So this one of the big ideas on generators, is you know, you can package up iteration into little 
- functions and if you're using iteration you actually get a lot of power for how things kind of fit together and 
- how you can do data processing in your program.


### video 4
Alright, in this project, I want to look at one of the more powerful features of generators, which is the ability 
to set up processing pipelines and workflows. And to set that up, I want to return to Unix for a second. One 
of the things that we did, is we wrote a Python function that emulated the behavior of the Unix tail -f command. 
Just to see that, what we did is we did a tail -f, and we were watching a file as data was being written to it. 
This is the kind of thing that you would use again to watch maybe a web server log, or something like that. So 
in this case I'm watching stock market data. One of the more powerful features of Unix though, is that you can 
set up pipes, like you can take the output of one command and pipe it into another command. So, maybe I can do 
something like this, right, so like, I could say, I'm gonna take the tail -f, and I'm gonna pipe it into a function 
that looks for just certain substrings. What's going on now is I'm following the file, but I'm only interested in 
those stock names, IBM, Microsoft, CAT and AA. It turns out that I can do a similar thing to that using generators, 
here's how you might go about doing that. Do an example here. So, first of all, I'm gonna run this little follow 
program that I have. The code at the top, I've got this follow function. What I'm gonna do, is go ahead and start 
this again, so I'm gonna say, OK, let's follow this file, stocklog.csv. That is a generator that comes back, keep 
in mind the follow function up here is using the yield statement, that makes it one of these generator objects. 
If you call next on it, you're gonna see it pop out lines of data. One of the things that you can do, is you can 
take that data and start to feed it into other functions that work with the for loop. This might kind of blow your 
mind a little bit, but one of the things that I could do is feed this into the csv module. This is something that 
we worked with earlier, to parse csv files, so what I could do is I could say a rows is equal to csv.reader of 
lines. Turns out that this rows object also knows how to do iteration. So what's happening now, is the data from 
this follow function is going into the csv.reader, and it's coming out as rows that have been split up and kind 
of cleaned up, and that's kind of interesting. I could then take that one step further, maybe I could write 
like a grep function, where you give me some stock names and some rows, and then what I'll do is I'll do a 
little for loop, like I'll say for row in rows, if row zero is in names, yield row. What's happening here is 
I have a function that's pulling in data, looking for something, and then emitting something that is a match. 
So then what I could do here is I could say, you know, matching is equal to grep, where I give it a set of 
stock names, like IBM, Microsoft, CAT and AA, I think that's what I used earlier on rows. This is also a generator 
object, if I start calling next on it, you'll start seeing it emitting rows for just those stocks. I've essentially 
done exactly the same thing that I did in that Unix example, it's the follow function is feeding that csv.reader 
that I've set up here, and then that is feeding this grep function, and we're getting like a bunch of things 
kind of popping out. You can extend this idea even further, and maybe do things like type conversion on these 
fields. This is a more advanced thing, well let's make a little list here, types, it looks like we have a string, 
a float, what I'm doing is looking at the data and matching up types. I'm just going straight across, we have 
a string, we have a float, we have a string, a string, and then it looks like a bunch of floats. After that I could 
do something like this, I could say, well, you know the converted values is equal to a generator expression where 
I do type conversion. We have a generator object, if you call next on that, now what you're getting is you're 
getting a bunch of data that has been converted, you're seeing it's no longer as strings. I could get the negative 
change, I could say, well, these are all the rows in converted, if row four is less than zero, that's that idea. 
I forgot a for statement in there. Now you have a generator which is only producing negative change events on it, 
but only for those stocks that are in that list. This is a very powerful idea that's taking place here, I mean 
essentially what you can start doing are writing programs that use this technique to kind of set up little workflow 
things, you know, looking for negative change, looking for, you know, doing type conversion, doing csv parsing, 
and so forth. You might be able to package all these ideas up into a function, like up here, I could say, let's 
make a function parse_stock_data, where you give me some lines, I don't even really care where those lines are 
coming from, but what I'm gonna do is just set up a pipeline, I'll say rows is equal to csv.reader of lines, and 
then maybe I'll do the types thing, like the type with a string, a float, string, string, float, float, float, int, 
I believe, OK, so we had something like that. I could say converted is equal to that type conversion trick. Maybe 
I return that back, and then we start writing little workflows on that, maybe say lines is equal to follow 
Data/stocklog.csv, and then rows is equal to parse_stock_data lines. And then maybe negative change is equal to, 
you know, row for row in rows if row four is less than zero. And then you start writing for loops on it, it's 
kind of an amazing sort of thing that you can do here. This is only giving a small taste of what's possible, 
this idea of workflows actually applies to a wide range of problems involving data processing and other tasks. 
I've got a little bug in my string formatting there, but let's modify it and see if it works here. OK, so that's a 
little bit more of an advanced use of generators, is that, essentially you can customize for loop, but then you get 
into these workflows and pipelines. Very interesting kind of way to program and structure data processing tasks.