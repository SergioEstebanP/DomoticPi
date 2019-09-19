var express = require("express");
var app = express();

app.listen(3000, () => {
	 console.log("Device service running on port 3000");
});

app.get("/dogs", (req, res, next) => {
	 res.json(
		[
			{
				"group_0": {
					"name": "pipo",
					"age": 4
				}
			},
			{
				"group_1": {
					"name": "tobi",
					"age": 5
				}
			}
		]
	 );
});
