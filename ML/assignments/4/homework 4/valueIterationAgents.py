# valueIterationAgents.py
# -----------------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


import mdp, util, random

from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
		"""
				* Please read learningAgents.py before reading this.*

				A ValueIterationAgent takes a Markov decision process
				(see mdp.py) on initialization and runs value iteration
				for a given number of iterations using the supplied
				discount factor.
		"""
		def __init__(self, mdp, discount = 0.9, iterations = 100):
				"""
					Your value iteration agent should take an mdp on
					construction, run the indicated number of iterations
					and then act according to the resulting policy.

					Some useful mdp methods you will use:
							mdp.getStates()
							mdp.getPossibleActions(state)
							mdp.getTransitionStatesAndProbs(state, action)
							mdp.getReward(state, action, nextState)
							mdp.isTerminal(state)
				"""
				self.mdp = mdp
				self.discount = discount
				self.iterations = iterations
				self.values = util.Counter() # A Counter is a dict with default 0

				# Write value iteration code here

				mdpStates = self.mdp.getStates()
				k = self.iterations

				for j in range(k):
						for i in mdpStates:
								if self.mdp.isTerminal(i):
										self.values[i] = self.mdp.getReward(i, 'north', (0, 0))
										continue
								possActions = self.mdp.getPossibleActions(i)
								res = -1e5
								for a in possActions:
										trans = self.mdp.getTransitionStatesAndProbs(i, a)
										temp = 0.0
										for ns in trans:
												temp += ns[1] * (self.mdp.getReward(i, a, ns[0]) + (self.discount * self.values[ns[0]]))
										res = max(res, temp)
								self.values[i] = res


		def getValue(self, state):
				"""
					Return the value of the state (computed in __init__).
				"""
				return self.values[state]


		def computeQValueFromValues(self, state, action):
				"""
					Compute the Q-value of action in state from the
					value function stored in self.values.
				"""
				res = 0.0
				trans = self.mdp.getTransitionStatesAndProbs(state, action)
				for ns in trans:
						res += ns[1] * (self.mdp.getReward(state, action, ns[0]) + self.discount * self.values[ns[0]])
				return res												

		def computeActionFromValues(self, state):
				"""
					The policy is the best action in the given state
					according to the values currently stored in self.values.

					You may break ties any way you see fit.  Note that if
					there are no legal actions, which is the case at the
					terminal state, you should return None.
				"""
				res = 0
				max_prob = -1e5
				possActions = self.mdp.getPossibleActions(state)
				for i in possActions:
						curr = 0.0
						trans = self.mdp.getTransitionStatesAndProbs(state, i)
						for nextState in trans:
								curr += nextState[1] * (self.mdp.getReward(state, i, nextState[0]) + self.discount * self.values[nextState[0]])
						if curr > max_prob:
								max_prob = curr
								res = i
				return res

		def getPolicy(self, state):
				return self.computeActionFromValues(state)

		def getAction(self, state):
				"Returns the policy at the state (no exploration)."
				return self.computeActionFromValues(state)

		def getQValue(self, state, action):
				return self.computeQValueFromValues(state, action)
