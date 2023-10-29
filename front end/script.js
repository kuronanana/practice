let users = []; // 宣告一個陣列users

function register() {
	let username = document.getElementById("username").value;  // 獲取用戶名
	let age = document.getElementById("age").value;  // 獲取年齡
	let gender = document.getElementById("gender").value;  // 獲取性別
	let hobbies = [];
	if (document.getElementById("hobby1").checked) {
		hobbies.push(document.getElementById("hobby1").value);
	}

	if (document.getElementById("hobby2").checked) {
		hobbies.push(document.getElementById("hobby2").value);
	}

	if (document.getElementById("hobby3").checked) {
		hobbies.push(document.getElementById("hobby3").value);
	}

	if (!username  || !age  || !gender ) {
	    document.getElementById("message").innerHTML = "Please fill in all required fields!";
	    return;
	}
    
	if (age >= 18) {
	    document.getElementById("message").innerHTML = username + " is an adult.";
	} else {
	    document.getElementById("message").innerHTML = username + " is not an adult.";
	}

	let user = {   // 宣告一個user物件
		name:username,
		age:age,
		gender:gender
	};

	users.push(user); // 將user物件放到users陣列最後方
	document.getElementById("message").innerHTML = `Thanks for registering, ${username}! You are user number ${users.length}.Your hobbies are ${hobbies.join(", ")}.`;
    }
    
document.getElementById("myButton").addEventListener('click',function(){
	document.getElementById("myDiv").innerHTML = "hello!";

})

document.getElementById("toggleButton").addEventListener('click',function(){
	document.getElementById("content").classList.toggle('highlight');

})

const number = [1,2,3,4]
setTimeout(function(){
	const doubled = number.map(function(item){
		return item * 2;
	});
	console.log(doubled);
},2000);

