var age1 = 20

{
    let age = 89;
    console.log(age)
}
console.log(age1)


let name1 = 'Piyush'
function solve(name, age) {
    return console.log("Name is: " + name + " and " + "age is: " + age)
}

solve(name1, age1)

"use strict";
x = 3.14;
console.log(x)


var name2 = "baby";
const person = {
    name: 'Piyush',
    agee: 22,
    greet() {
        console.log("hi, my name is: " + this.name)
    }
}
person.greet();

console.log("\n")
console.log("------------------------------------------ARRAY------------------------------------------------------")
console.log("\n")

// Array objects & reference operator
const hobbies = ['sports', 'Cooking'];
for (let hobby of hobbies) {
    console.log(hobby);
}
console.log(hobbies.map(hobby => 'Hobby: ' + hobby));
console.log(hobbies);

hobbies.push("Programming");
console.log(hobbies);


console.log("\n")
console.log("-------------------------------------SPREAD & REST Operators------------------------------------------")
console.log("\n")

//Spread & Rest
const cpyarr = [...hobbies] //Spread Operator
console.log(cpyarr);

const toarr = (...args) => { //Rest Operator
    return args;
}
console.log(toarr(1, 2, 3))

console.log("\n")
console.log("-----------------------------MUST LOOK AT THE CODE OF DESTRUCTURING-----------------------------------")
console.log("\n")