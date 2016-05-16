import re


PREP = 'PREP'
VERB = 'VERB'
DETR = 'DETR'


class Interpreter:
	def __init__(self):
		self.token_exprs = [
			(r'[ \n\t]+', None),
			(r'#[^\n]*', None),
			(r'AT', PREP),
			(r'TO', PREP),
			(r'DOWN', PREP),
			(r'UP', PREP),
			(r'IN', PREP),
			(r'INSIDE', PREP),
			(r'ON', PREP),
			(r'OFF', PREP),
			(r'UNDER', PREP),
			(r'ABOVE', PREP),
			(r'THE', DETR),
			(r'A', DETR),
			(r'AN', DETR),
			(r'MY', DETR),
			(r'ALL', DETR),
			(r'ANY', DETR),
			(r'GO', VERB),
			(r'WALK', VERB),
			(r'TURN', VERB),
			(r'LOOK', VERB),
			(r'EXAMINE', VERB),
			(r'TOUCH', VERB),
			(r'TALK', VERB),
			(r'ATTACK', VERB),
			(r'SAY', VERB)
		]

	def tokenize(self, command):
		pos = 0
		tokens = []

		while pos < len(command):
			token_match = False

			for expr in self.token_exprs:
				pattern, tag = expr
				r = re.compile(pattern)
				token_match = r.match(command, pos)

				if token_match:
					value = token_match.group(0)

					if tag:
						token = (value, tag)
						tokens.append(token)
					break

			if not token_match:
				break
			else:
				pos = token_match.end(0)

		return tokens