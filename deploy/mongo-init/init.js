conn = new Mongo({ useUnifiedTopology: true });
db = conn.getDB("beacon");


// db.beacon.createIndex({ "address.zip": 1 }, { unique: false });
// db.beacon.insert({ "address": { "city": "Paris", "zip": "123" }, "name": "Mike", "phone": "1234" });
// db.beacon.insert({ "address": { "city": "Marsel", "zip": "321" }, "name": "Helga", "phone": "4321" });

// Create collections


db.createCollection("datasets");
db.createCollection("individuals");


// Create indexes for all the entities in the database

db.datasets.createIndex([('$**', 'text')]);
db.individuals.createIndex([('$**', 'text')]);
