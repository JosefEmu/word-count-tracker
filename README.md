# Word Count Tracker
You have an .docx to write and want to keep track of your word count against your target?

It's a simple tool that copies tet from .docx to .txt and further counts the number of your words you've written so far.

<h3> Commandline </h3>

```bash
pip install docx2txt

cd word_count_tracker
```

<h3> In Python </h3>

```python
import word_count_tracker as wct
```

_You can also change the timer from the default 300secs intervals as you wish:_
```python
wct.TIMER = 1 #Input seconds as integers
```

Run the "run_it" method and input the full URL for your .docx file when prompted...

```python
wct.run_it()
```


### _You're good to go!!_
