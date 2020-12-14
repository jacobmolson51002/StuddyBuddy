const functions = require('firebase-functions');
const express = require('express');
const engines = require('consolidate');
var hbs = require('handlebars');
const admin = require('firebase-admin');

const app = express();
app.engine('hbs',engines.handlebars);
app.set('views','./views');
app.set('view engine','hbs');

/*var serviceAccount = require("./thestuddybuddy-64eb1-firebase-adminsdk-5ywxk-09df351eb7.json");
admin.initializeApp({
credential: admin.credential.cert(serviceAccount),
databaseURL: "firebase-adminsdk-5ywxk@thestuddybuddy-64eb1.iam.gserviceaccount.com"
});*/
admin.initializeApp(functions.config().firebase);

async function getFirestore(){
const firestore_con  = await admin.firestore();
const writeResult = firestore_con.collection('sample').doc('testDoc').get().then(doc => {
if (!doc.exists) { console.log('No such document!'); }
else {return doc.data();}})
.catch(err => { console.log('Error getting document', err);});
return writeResult
}

app.get('/',async (request,response) =>{
var db_result = await getFirestore();
response.render('index',{db_result});
});
exports.app = functions.https.onRequest(app);

























// // Create and Deploy Your First Cloud Functions
// // https://firebase.google.com/docs/functions/write-firebase-functions
//
// exports.helloWorld = functions.https.onRequest((request, response) => {
//   functions.logger.info("Hello logs!", {structuredData: true});
//   response.send("Hello from Firebase!");
// });


