import webbrowser
website = ['site1', 'site2', 'site3', 'site4']
for i in range(len(website)):
	site = 'http://' + website[i]
	webbrowser.open(site)