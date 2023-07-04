import { makeStyles } from '@material-ui/core/styles';
import Grid from '@material-ui/core/Grid';
import Paper from '@material-ui/core/Paper';
import Typography from '@material-ui/core/Typography';
import ButtonBase from '@material-ui/core/ButtonBase';
import { Button } from '@material-ui/core';
import Rating from '@material-ui/lab/Rating';
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import AppBarss from '../AppBar/appBar';
import Footer from '../Footer/footer';


const useStyles = makeStyles((theme) => ({
    root: {
        flexGrow: 1,
    },
    paper: {
        padding: theme.spacing(2),
        margin: 'auto',
        maxWidth: 350,
        maxHeight: 300,
        border: 'inset',
        marginTop: '9px',
        marginBottom: '9px',

    },
    image: {
        width: 128,
        height: 128,
    },
    img: {
        margin: 'auto',
        display: 'block',
        maxWidth: '100%',
        maxHeight: '100%',
    },
    btn: {
        backgroundColor: '#3f51b5',
        color: '#fff',
        "&:hover": {
            color: "#fff",
            backgroundColor: 'blue',
        }
    },
    category: {
        fontSize: '10px'
    },
    title: {
        fontSize: '14px',

    },
    footer: {
        marginTop: "auto !important",

    },
    contentContainer: {
        marginTop: theme.spacing(13), // Ajusta el valor según tus necesidades
    },
    contentContainerFooter: {
        marginTop: theme.spacing(22), // Ajusta el valor según tus necesidades
    },
    contentContainerFooterRes: {
        marginTop: theme.spacing(23), // Ajusta el valor según tus necesidades
    },

}));

/*await axios.get(process.env.API_BASE_URL + '/api/feed/?format=json')
    .then((response) => {
        console.log(response)
    })*/

export default function List_book(props) {
    const [data, setData] = useState([])
    const classes = useStyles();
    const params = new URLSearchParams(props.location.search);
    const search = params.get('search');
    console.log({ search })
    useEffect(() => {
        const callApi = async () => {
            await axios.get(`http://127.0.0.1:8000/siteapp/search/?search=${search}`,
            ).then((response) => {
                // console.log({ data: response.data })
                // console.log(response.data.length,'holaaaaaa')

                setData(response.data.books);
            })

        }
        callApi();
    }, []);
    return (
        (data?.length) ? (
            <>
                <AppBarss />
                <div className={classes.contentContainer}>
                    <Grid className={classes.root} container
                        direction="row"
                        justifyContent="center"
                        alignItems="center" item md={12}>
                        <h1 >Resultado de busqueda para: '{search}'</h1>

                    </Grid>

                    <Grid className={classes.root} container
                        direction="row"
                        justifyContent="center"
                        alignItems="center" item md={12}>

                        {data?.map((book, key) => (
                            <Grid item md={4} key={key}>
                                <Paper className={classes.paper}>
                                    <Grid container spacing={1}>
                                        <Grid item>
                                            <ButtonBase className={classes.image}>
                                                <img className={classes.img} alt="complex" src={book.image} />
                                            </ButtonBase>
                                        </Grid>
                                        <Grid item xs={12} sm container>
                                            <Grid item xs container direction="column" spacing={1}>
                                                <Grid item xs>
                                                    <Typography className={classes.title} gutterBottom variant="subtitle1">
                                                        {book.title}
                                                    </Typography>
                                                </Grid>
                                                <Grid item xs>
                                                    <Typography className={classes.category} gutterBottom variant="subtitle2">
                                                        {book.categorys.name}
                                                    </Typography>
                                                </Grid>

                                                {(book.calificacion) ? (
                                                    <Grid>
                                                        <Rating name="read-only" value={book.calificacion} readOnly />
                                                    </Grid>
                                                ) : (<></>)}

                                                <Grid item>
                                                    <Button className={classes.btn}>
                                                        <a href={`/view/${book.id}`} style={{color:"white"}}>Ver Libro</a>
                                                    </Button>
                                                </Grid>
                                            </Grid>

                                        </Grid>
                                    </Grid>
                                </Paper>
                            </Grid>
                        ))}

                    </Grid>
                    <div className={classes.contentContainerFooterRes}>
                        <Footer />
                    </div>
                </div>
            </>
        ) : (<>
            <AppBarss />
            <div className={classes.contentContainer}>
                <Grid className={classes.root} container direction="row" justifyContent="center" alignItems="center" item md={12}>
                    <h1>La búsqueda no ha devuelto ningún resultado.</h1> 
                </Grid>
                <br/>
                <div style={{ textAlign: 'center' }}>
                    <img src="https://cdn-icons-png.flaticon.com/512/1079/1079536.png?w=740&t=st=1687108258~exp=1687108858~hmac=a4350af8bc413c470ad79ab80ab1bd0ab1dec4a6a8e9ffcc736c42fc4831aea9" alt="Imagen" style={{ width: '200px', height: 'auto' }} />
                </div>
                <div className={classes.contentContainerFooter}>
                    <Footer />
                </div>
            </div>
        </>)


    );
}