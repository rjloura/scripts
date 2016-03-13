function sortArrayOfObjs(a, field) {

	/* Dont sort, just return */
	if (!a[0].hasOwnProperty(field))
		return a;

	if (sorted === field)
		return a.reverse();
	sorted = field;

	switch (typeof a[0][field]) {
		case 'string':
			return a.sort(function(x, y) {
				var xf = x[field].toLowerCase();
				var yf = y[field].toLowerCase();
				if (xf < yf)
					return (-1);
				if (xf > yf)
					return (1);
				return (0);
			});
		case 'number':
			return a.sort(function(x, y) {
				return (x[field] - y[field]);
			});
		default:
			return (a);
	}
}
	
var sorted = '';

var arr = 
[ {
	'name': 'Rui',
	'age': "3.2",
	'address': "NH"
}, {
	'name': 'diana',
	'age': "3.3",
	'address': "AL"
}, {
	'name': 'adam',
	'age': "4.0",
	'address': "TX"
} ];

console.log('name');
console.log(sortArrayOfObjs(arr, 'name'));
console.log('age');
console.log(sortArrayOfObjs(arr, 'age'));
console.log('age again');
console.log(sortArrayOfObjs(arr, 'age'));
console.log('addr');
console.log(sortArrayOfObjs(arr, 'address'));
