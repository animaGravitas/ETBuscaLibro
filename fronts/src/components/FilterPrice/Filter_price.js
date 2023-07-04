import React, { useState, useEffect } from 'react';
import Box from '@mui/material/Box';
import Slider from '@mui/material/Slider';
import Typography from '@mui/material/Typography';


function valuetext(value) {
    return `${value}°C`;
}

const minDistance = 10;

function formatPrice(price) {
    const formatter = new Intl.NumberFormat('es-CL', {
        style: 'currency',
        currency: 'CLP',
    });

    return formatter.format(price);
}
export default function FilterPrice({ callApi, currentPage, setData, setCountPage, currentCategory }) {
    const [priceRange, setPriceRange] = useState([0, 100]); // Estado inicial: rango de precios de 0 a 100
    let lastPriceRange = priceRange; // Estado para almacenar el último dato de priceRange
    useEffect(() => {
        lastPriceRange = priceRange; // Actualizar el último rango de precios cada vez que priceRange cambie
        console.log('Último rango de precios:', lastPriceRange);
    }, [priceRange]);


    const handlePriceChange = (event, newValue) => {
        setPriceRange(newValue);
        console.log({ newValue });
        callApi(currentCategory, currentPage, setData, setCountPage, newValue[0], newValue[1]);


    };

    return (
        <Box sx={{ width: 300 }}>
            <Slider
                value={priceRange}
                min={0}
                max={100000}
                step={10}
                onChange={handlePriceChange}
            />
            <Typography variant="body2">
                Precio: {formatPrice(priceRange[0])} - {formatPrice(priceRange[1])}
            </Typography>



        </Box>
    );
}