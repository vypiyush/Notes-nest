//Async JS Programming
//Callbacks, Promises, Async & await

// EXTRA NOTE: CLOSURES: ALWAYS HAVE ANONYMOUS-FUNCTION(FUNC WITH NO-NAME) {IMP-"CLOSURES"}

const datas= [

  {name:"Piyush", Hobby:"Meditation"},
  {name:"Raj", Hobby:"Software Devlopment"}

];

function getdatas(){
    setTimeout(() =>{
        let output = "";
        datas.forEach((data, index) => {
            output+=  `<li>${data.name}</li>`
        })
        document.body.innerHTML = output
    }, 1000);
}

/*
// Problem Statement

function createdata(newdata){
    setTimeout(() => {
        datas.push(newdata);
    }, 2000)
}
createdata({name:"Kumar", Hobby:"Seva"})
getdatas();
*/

/*
// Callbacks

function createdata(newdata, Callback){
    setTimeout(() => {
        datas.push(newdata);
        Callback();
    }, 2000)
}
createdata({name:"Kumar", Hobby:"Seva"}, getdatas)

*/

// Same Code for both (Promises) and (Async & await)
function createdata(newdata){
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            datas.push(newdata);
            let error = false;
            if(!error){
                resolve();
            }else{
                reject("Kuch sahi nai hai...")
            }
        }, 2000)
    })
}

// Promises

createdata({name:"Kumar", Hobby:"Seva"})
.then(getdatas)                          // For resolve
.catch(err => console.log(err))          // For reject

//Async & await

async function start(){
    await createdata({name:"Kumar", Hobby:"Seva"})  // await only used with async
    getdatas();
}
start();