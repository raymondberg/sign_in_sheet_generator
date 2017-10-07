## Sign In Sheet Generator

I hate generating sign-in-sheets. Do you?

This might help.


## Install

```
pip install -r requirements.txt
```

## Usage

It generates a pdf. Pretty straight forward.

```
python generate.py -t "Cool event" -s "Doors at 6:00pm" -i /path/to/source/file
```

The default behavior is to use the first column from a given CSV. You can specify a column title if you need.

```
python generate.py -t "Cool event" -s "Doors at 6:00pm" -i /path/to/source/file -c "Full Name"
```

There are other options; spelunk a bit!
