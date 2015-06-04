# sublcmd

A wrapper for the `subl` command which opens Sublime Text. It supports passing
data to stdin on platforms other than OSX.


## Usage

```
$ pip install git+https://bitbucket.org/ucamhal/sublcmd.git
$ export SUBL=/usr/bin/subl  # Or wherever it is
$ echo hi | subl  # Open sublime text with 'hi' in a new tab
```
