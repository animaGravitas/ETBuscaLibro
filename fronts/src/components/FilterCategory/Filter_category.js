import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { makeStyles } from '@material-ui/core/styles';
import Grid from '@material-ui/core/Grid';
import Paper from '@material-ui/core/Paper';
import Typography from '@material-ui/core/Typography';
import ButtonBase from '@material-ui/core/ButtonBase';
import { Button } from '@material-ui/core';
import Rating from '@material-ui/lab/Rating';
import Footer from '../Footer/footer';
import AppBarss from '../AppBar/appBar';
import Divider from '@material-ui/core/Divider';
import Pagination from '@material-ui/lab/Pagination';
import FilterCategory from '../FilterCategory/Filter_category';
import Select from '@material-ui/core/Select';
import MenuItem from '@material-ui/core/MenuItem';
import FormControl from '@material-ui/core/FormControl';
import InputLabel from '@material-ui/core/InputLabel';

const useStyles = makeStyles((theme) => ({
    btn: {
        backgroundColor: '#3f51b5',
        color: '#fff',
        boxShadow: "2px 2px 2px black",
        "&:hover": {
            color: "#fff",
            backgroundColor: 'blue',
        }
    },
    root: {
        marginLeft: "22px",
    },
    formControl: {
        margin: theme.spacing(1),
        minWidth: 120,
    },
    selectEmpty: {
        marginTop: theme.spacing(2),
    },
}));

export default function CategoryFilter(callApi, currentPage, setData, setCountPage, setCurrentCategory, currentCategory) {
    const [selectedCategory, setSelectedCategory] = useState(null);
    const classes = useStyles();
    const [age, setAge] = useState('');

    useEffect(() => {
        if (selectedCategory !== null) {
            const newURL = `http://localhost:3000/category/${selectedCategory}`;
            window.location = (null, '', newURL);
        }
    }, [selectedCategory]);

    const handleCategoryClick = (category) => {
        setSelectedCategory(category);
    };

    const handleChange = (event) => {
        callApi(event.target.value, currentPage, setData, setCountPage);
        setCurrentCategory(event.target.value)
    };

    return (
        <Grid className={classes.root} container direction='row' justifyContent='flex-start' alignItems="baseline" item md={6}>
            <FormControl className={classes.formControl}>
                <InputLabel id="demo-simple-select-label">Categorias</InputLabel>
                <Select
                    className={classes.selectEmpty}
                    inputProps={{ 'aria-label': 'Without label' }}
                    value={currentCategory}
                    onChange={handleChange}
                    labelId="demo-simple-select-label"
                    id="demo-simple-select"
                >
                    {/*<MenuItem value={0}>
                        <em>None</em>
                    </MenuItem>*/}
                    {/*<MenuItem value={1} onClick={() => handleCategoryClick(1)}>Computación e Informática</MenuItem>*/}
                    <MenuItem value={2} onClick={() => handleCategoryClick(2)} >Mundo Cómic</MenuItem>
                    {/*<MenuItem value={3} onClick={() => handleCategoryClick(3)} >Literatura</MenuItem>*/}
                    {/*<MenuItem value={4} onClick={() => handleCategoryClick(4)} >Infantil y Juvenil</MenuItem>*/}
                    {/*<MenuItem value={5} onClick={() => handleCategoryClick(5)} >Viaje y Turismo</MenuItem>*/}
                    {/*<MenuItem value={6} onClick={() => handleCategoryClick(6)} >Cuerpo y Mente</MenuItem>*/}
                    {/*<MenuItem value={7} onClick={() => handleCategoryClick(7)} >Economía y Administración</MenuItem>*/}
                    <MenuItem value={8} onClick={() => handleCategoryClick(8)} >Ciencias</MenuItem>
                    <MenuItem value={9} onClick={() => handleCategoryClick(9)} >Más Vendidos</MenuItem>
                    <MenuItem value={10} onClick={() => handleCategoryClick(10)} >Novedades</MenuItem>
                </Select>
            </FormControl>
        </Grid>
    );
}         