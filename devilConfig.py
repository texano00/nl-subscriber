devilConfig = [
	{
		"url" : "https://www.dezeen.com/newsletters/",
		"waitUntilThisElement" : "#fieldEmail",
		"emailElement" : "#fieldEmail",
		"submitElement" : 'div.subscribe-box-inner:nth-child(1) > form:nth-child(3) > input:nth-child(5)',
		"isInsideIframe" : False,
		"iframeElement" : "",
		"checkboxes" : [
		] 
		
	},
	{
		"url" : "http://www.feltrinellieditore.it/newsletter/",
		"waitUntilThisElement" : "#id_email",
		"emailElement" : "#id_email",
		"submitElement" : ".btn",
		"isInsideIframe" : False,
		"iframeElement" : "",
		"checkboxes" : [
		] 
		
	},
	{
		"url" : "http://www.ovs.it/LandingNewsletter.html",
		"waitUntilThisElement" : "#primary > section > div.content-asset > iframe",
		"emailElement" : "#newsletter_email",
		"submitElement" : "#new_newsletter > div.row > div > div > div.input-wrapper > div.input-submit > input",
		"isInsideIframe" : True,
		"iframeElement" : "#primary > section > div.content-asset > iframe",
		"checkboxes" : [
			"#newsletter_privacy"
		] 
		
	}
]