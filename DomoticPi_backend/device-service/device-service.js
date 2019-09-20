const express = require("express");
const mysql = require("mysql")
const credentials = require("../global-config/credentials.json")
const config = require('../global-config/services-config.json')

// configuration
const DEVICE_SERVICE_PORT = config.ports.services_ports.device_service
const MYSQL_PORT = config.ports.mysql
const SERVER_RUNNING_MESSAGE = 'Device service running on PORT: '
const MYSQL_PASSWORD = credentials.mysql

app = express();

app.listen(DEVICE_SERVICE_PORT, () => {
	 console.log(SERVER_RUNNING_MESSAGE + DEVICE_SERVICE_PORT);
});

// mysql data access
const connection = mysql.createConnection({
	host: 'localhost',
	user: 'device-service',
	password: 'device-service',
	database: 'devicesDB',
	port: MYSQL_PORT,
	insecureAuth: true
})


// GET /devices
app.get("/devices", (req, res, next) => {
	connection.connect()
	connection.query('SELECT * from device', function(error, results, fields) {
		if (error) throw error
		console.log(results)
	})
	res.json({
		"message": 200
	});
	connection.end()
});