>18: 	'''Definition d'une classe et donc d'un HMM comme étant un objet, calcul et etiration via l'algorithme de Baum Welch'''
>19: 	
>20: 	def __init__(self, listObservables, count):
>21: 		'''initialisation du hmm'''

<22: 		self.states = listOfStates

<40: 		self.gamma = range(len(self.listObservables))
<41: 		for index in range(len(self.beta)):
<42: 			dictOfStates = {}
<43: 			for key in self.states:
<44: 				dictOfStates[key] = 0.0
<45: 			self.gamma[index] = dictOfStates
<46: 

>43: 		'''Initialisation du hmm lambda_0 et premier calcul pour les probabilites de transitions, emissions et initiales (equiprobabilité partout)'''
>44: 		self.states = encod.get_categories(data+"/voc_etats")

>65: 		'''Calcul des alpha(i,t) tels que definis dans les slides,  correspond à la probabilité de se trouver dans
>66: l’etat i du HMM lambda a un instant t, ayant observe la suite o1 . . . ot−1 '''

>82: 		'''Calcul des beta(i,t) tels que definis dans les slides, meme calcul que pour les alpha mais avec un parcours inverse du treillis.'''

<99: 		# iterate forward #
<100: 		for index in range(len(self.listObservables)):
<101: 			for j in self.states:
<102: 				sumGamma = 0.0
<103: 				for etat in self.states:
<104: 					sumGamma = sumGamma + self.alpha[index][etat]*self.beta[index][etat]
<105: 				#self.gamma[index][j] = 0.0
<106: 				if not sumGamma == 0.0:
<107: 					self.gamma[index][j] = (self.alpha[index][j]*self.beta[index][j])/sumGamma
<108: 

<110: 

<112: 		for state in self.states:
<113: 			self.Pi[state] = self.gamma[0][state]

<116: 		#init proba pt for the calcul of transition probabilities
<117: 		p = range(len(self.listObservables)-1)
<118: 		for index in range(len(p)):
<119: 			p[index] = {}
<120: 			for i in self.states:
<121: 				p[index][i] = {}
<122: 				for j in self.states:
<123: 					p[index][i][j] = 0.0
<124: 
<125: 		#calcul of partiel transition proba
<126: 		for t in range(len(p)):
<127: 			for i in self.states:
<128: 				sumOnStates = 0.0
<129: 				for j in self.states:
<130: 					sumOnStates = sumOnStates + self.alpha[t][j]*self.beta[t][j]
<131: 					p[t][i][j] = self.alpha[t][j]*self.beta[t+1][j]*self.emissions[self.listObservables[t]][j]*self.transitions[i][j]
<132: 				for j in self.states:
<133: 					#p[t][i][j] = 0.0
<134: 					if not sumOnStates == 0.0:
<135: 						p[t][i][j] = p[t][i][j]/sumOnStates
<136: 
<137: 		#calcul of transition probabilities
<138: 		for i in self.states:
<139: 			for j in self.states:
<140: 				sumOnP = 0.0
<141: 				sumOnGamma = 0.0
<142: 				for t in range(len(p)):
<143: 					sumOnP = sumOnP + p[t][i][j]
<144: 					sumOnGamma = sumOnGamma + self.gamma[t][i]
<145: 				#self.transitions[i][j] = 0.0
<146: 				if not sumOnGamma == 0.0:
<147: 					self.transitions[i][j] = sumOnP/sumOnGamma
<148: 
<149: 

<152: 		for observable in self.emissions:
<153: 			for state in self.states:
<154: 				sumGammaForObservable = 0.0
<155: 				sumGammaTotal = 0.0
<156: 				for t in range(len(self.listObservables)):
<157: 					sumGammaTotal = sumGammaTotal + self.gamma[t][state]
<158: 					if self.listObservables[t] == observable:
<159: 						sumGammaForObservable = sumGammaForObservable + self.gamma[t][state]
<160: 				#self.emissions[observable][state] = 0.0
<161: 				if not sumGammaTotal == 0.0:
<162: 					self.emissions[observable][state] = sumGammaForObservable/sumGammaTotal

<165: 		for i in range(self.iterationCount):
<166: 			self.setAlpha()
<167: 			self.setBeta()
<168: 			self.setGamma()
<169: 			self.setPi()
<170: 			self.setT()
<171: 			self.setE()
