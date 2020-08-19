# ESP8266-Webpage-Formatter
Simple python module to format regular html code into a string for ESP8266 webserver

#NOTE: I have not tested this for all cases of html formatting. Please ensure that the converted code matches what you would expect
To know if it worked properly, all quotation marks inside the html should be escaped with a back slash preceding it. Each line should should start and end with a single quote mark

Start by writing regular html code that can be tested for format and save as .txt when done. Then run the program in a python shell to convert the file to a string that can be copied and pasted into arduino code directly to be used with ESP8266 Webserver

example:
This was the python prompt and answers that were used to generate the code:

Enter the file name of the file to convert: Main.txt
Enter the name of the page to be converted: MAIN_page

This is the code contained in Main.txt:

<html>
	<title>First Web Server</title>
	<head>
		<body>
			<form method = "get">
			<input type = "submit" name = "led" value = "ON">
			<input type = "submit" name = "led" value = "OFF">
			</form>
		</body>
	</head>
</html>

Previous code will be converted to the following for copy and paste:

String MAIN_page =
"<html>"
	"<title>First Web Server</title>"
	"<head>"
		"<body>"
			"<form method = \"get\">"
			"<input type = \"submit\" name = \"led\" value = \"ON\">"
			"<input type = \"submit\" name = \"led\" value = \"OFF\">"
			"</form>"
		"</body>"
	"</head>"
"</html>";
