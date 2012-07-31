# urls

Mac OS X command line tool to extract and process URLs found in text.

## Usage

	urls - A quick and dirty url parser and processor.
	
	Usage:
	  urls [<text> [--copy] [--open] [--twitter] [--no-output] [--html] [--debug]]
	  urls -h | --help
	  urls --version
	
	Options:
	  -h --help       Show this screen.
	  -c --copy       Copy the first URL found in the text to the pasteboard.
	  -o --open       Open the first URL found in the text.
	  -t --twitter    Parse text for twitter usernames and hashtags and convert them to twitter URLs
	  -n --no-output  Do not output urls'
	  --debug         Debug on!

## Examples

Extract a simple URL from a command line parameter.

	$ urls 'http://apple.com'

Open it in a web browser:

	$ urls 'http://apple.com' --open

Look for twitter addresses:

	$ urls '@schwa Hello!' --twitter
	http://twitter.com/schwa

Look for URLs on standard input

	$ cat somefile.text | urls

What remote urls does this git repository use?

	$ urls-python$ git remote -v 
	origin	https://github.com/schwa/urls-python (fetch)
	origin	https://github.com/schwa/urls-python (push)

Now filter them through urls:

	$ urls-python$ git remote -v | urls
	https://github.com/schwa/urls-python

And copy them directory to the pasteboard

	$ urls-python$ git remote -v | urls --copy
	https://github.com/schwa/urls-python

## Installation

	python setup.py install --user

## License

Copyright (c) 2012, Jonathan Wight
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met: 

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer. 
2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution. 

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

The views and conclusions contained in the software and documentation are those
of the authors and should not be interpreted as representing official policies, 
either expressed or implied, of the FreeBSD Project.
