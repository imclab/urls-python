#!/usr/bin/env python
# coding=utf-8

"""urls - A quick and dirty url parser and processor.

Usage:
  urls [<text> [--copy] [--open] [--twitter] [--no-output] [--html] [--debug]]
  urls -h | --help
  urls --version

Options:
  -h --help       Show this screen.
  -c --copy     Copy the first URL found in the text to the pasteboard.
  -o --open       Open the first URL found in the text.
  -t --twitter    Parse text for twitter usernames and hashtags and convert them to twitter URLs
  -n --no-output  Do not output urls'
  --debug         Debug on!
"""

# Other ideas
#  --html          Convert the input to marked up HTML

import re
import sys

import docopt # pip install --user docopt
import ttp # https://github.com/BonsaiDen/twitter-text-python/
import envoy # pip install --user envoy

################################################################################

theParser = ttp.Parser()

# git@github.com:schwa/CoreTextToy.git

thePatterns = [
	{ 'pattern': re.compile(r'git@.+:.+?\.git'), 'stop': True },

	# From http://daringfireball.net/2010/07/improved_regex_for_matching_urls
	{ 'pattern': re.compile(r'''(?i)\b((?:[a-z][\w-]+:(?:/{1,3}|[a-z0-9%])|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))'''), 'stop': False},
	]

def URLsForString(s, twitter = False):
	theURLs = []
	
	# Use twitter parsing...
	result = theParser.parse(s)

	theURLs += result.urls

	if twitter:
		for theUser in result.users:
			theURLs.append('http://twitter.com/%s' % theUser)
		for theTag in result.tags:
			theURLs.append('http://twitter.com/#!/search/#%s' % theTag)

	# Use some crude
	for thePatternDict in thePatterns:
		thePattern = thePatternDict['pattern']
		theResults = re.findall(thePattern, s)
		if theResults:
			p = [theResult if type(theResult) == type('') else theResult[0] for theResult in theResults]
			theURLs += p
			if thePatternDict['stop']:
				break

	return theURLs

def main():
	arguments = docopt.docopt(__doc__, version='urls 0.1')

	if arguments['--debug']:
		print(arguments)
	
	theText = arguments['<text>']
	if not theText:
		theText = sys.stdin.read()

	theURLs = URLsForString(theText, twitter = bool(arguments['--twitter']))
	if not theURLs:
		if not theText:
			sys.stderr.write('# No URLs found on standard input\n')
		else:
			sys.stderr.write('# No URLs found\n')
	else:
		if not arguments['--no-output']:
			print '\n'.join(set(theURLs))

	if arguments['--copy']:
		theCommand = 'echo \'%s\' | pbcopy' % theURLs[0]
		envoy.run(theCommand)

	if arguments['--open']:
		envoy.run('open \'%s\'' % theURLs[0])

################################################################################
	
if __name__ == '__main__':
	main()
