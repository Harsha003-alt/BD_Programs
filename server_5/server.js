const express = require('express');

const app = express();
app.use(express.json());

let products = [
    { id: 1, name: 'Laptop', price: 75000 },
    { id: 2, name: 'Mouse', price: 500 },
    { id: 3, name: 'Keyboard', price: 1200 }
];

let nextId = 4;

// GET - Get all products
app.get('/products', (req, res) => {
    res.json(products);
});

// POST - Add a new product
app.post('/products', (req, res) => {
    const product = {
        id: nextId++,
        name: req.body.name,
        price: req.body.price
    };

    products.push(product);

    res.status(201).json(product);
});

// Start server
app.listen(3000, () => {
    console.log('Server running on Port 3000');
});