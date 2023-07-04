import { Button } from '@material-ui/core';
import { Paper } from '@material-ui/core';

import { makeStyles } from '@material-ui/core/styles';
import { Grid } from '@material-ui/core';
import Card from '@material-ui/core/Card';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import Typography from '@material-ui/core/Typography';
import ButtonBase from '@material-ui/core/ButtonBase';
import Rating from '@material-ui/lab/Rating';
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import List_book from '../ViewBook/List_book';
import { render } from "react-dom"
import { Router, Link } from "@reach/router"





const useStyles = makeStyles((theme) => ({

    carousel: {

    },
    img_carousel: {
        width: '128px',
        height: '149px'

    },
    book: {
        marginTop: '33px',

    },

    card: {
        width: '1000px',
        height: '1000px',
        border: 'inset',
    },
    paper: {
        padding: theme.spacing(2),
        margin: 'auto',
        maxWidth: '1000px',
        maxHeight: '1000px',
        border: 'inset',
        marginTop: '9px',
        marginBottom: '9px',

    },
    image: {
        width: 149,
        height: 149,
    },
    img: {
        margin: 'auto',
        display: 'block',
        maxWidth: '149px',
        maxHeight: '149px',
    },
    btn: {
        backgroundColor: '#3f51b5',
        color: '#fff',
        boxShadow: "2px 2px 2px black",
        "&:hover": {
            color: "#fff",
            backgroundColor: 'blue',
        }
    },
    category: {
        fontSize: '10px'
    },
    grid: {
        textAlign: 'initial',
    },
    title:{
        fontSize: '14px',
        fontWeight: 'bold'

    },
    gridCard:{
        width:"531px",
    },



}));


function Item({ item }) {
    const classes = useStyles();
    const preventDefault = (event) => event.preventDefault();

    return (
        <>
            <Grid container
                direction="row"
                justifyContent="center"
                alignItems="center" item md={10}>
                <Grid className={classes.book} item md={12}>
                    <Grid item md={12} >
                        <Paper className={classes.paper}>
                            <Grid className={classes.gridCard} container spacing={0} item md={12}>
                                <Grid item>
                                    <ButtonBase className={classes.image}>
                                        <img className={classes.img} alt="complex" src={item.image} />
                                    </ButtonBase>
                                </Grid>
                                <Grid className={classes.grid} item xs={12} sm container justifyContent='center'>
                                    <Grid item xs md={12} container direction="row" spacing={1}>
                                        <Grid container item xs md={12}>
                                            <Typography className={classes.title} gutterBottom variant="subtitle1">
                                                {item.title}
                                            </Typography>
                                        </Grid>
                                        <Grid item container xs md={12}>
                                            <Typography className={classes.category} gutterBottom variant="subtitle2">
                                                {item.editorial}
                                            </Typography>
                                        </Grid>
                                        <Grid item xs md={12}>
                                            <Typography className={classes.category} gutterBottom variant="subtitle2">
                                                {item.autor}
                                            </Typography>
                                        </Grid>
                                        <Grid item xs md={12}>
                                            <Typography className={classes.category} gutterBottom variant="subtitle2">
                                                {item.categorys.name}
                                            </Typography>
                                        </Grid>

                                        {(item.rating) ? (
                                            <Grid md={12}>
                                                <Rating name="read-only" value={item.rating} readOnly />
                                            </Grid>
                                        ) : (<></>)}

                                        <Grid item md={12}>
                                            <Button className={classes.btn}>
                                                <a href={`/view/${item.id}`} style={{color:"white"}}>Ver Libro</a>
                                            </Button>
                                        </Grid>
                                    </Grid>

                                </Grid>
                                <Grid item md={12} container alignItems='flex-end' justifyContent='flex-end'>
                                    
                                    <a href={`/category/${item.categorys.id}`} style={{ fontSize: 12 }}>
                                        Ver Más</a>


                                </Grid>
                            </Grid>
                        </Paper>
                    </Grid>
                </Grid>
            </Grid>
        </>

    )
}
export default Item