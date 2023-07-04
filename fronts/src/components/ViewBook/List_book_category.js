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
import FilterPrice from '../FilterPrice/Filter_price';





//import axios from 'axios';
//import { getUrl } from '@src/utils';
import { Link } from "@reach/router"



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
            backgroundColor: '#3f51b5',
        }
    },
    category: {
        fontSize: '10px'
    },
    price: {
        fontSize: '20px',
        fontWeight: 'bold'
    },
    store: {
        fontSize: '15px',
        fontWeight: '400'
    },
    title: {
        fontSize: '14px',

    },
    titlecategory: {
        textAlign: 'center',
    },
    divider: {
        margin: '35px',
    },
    rootPagination: {
        '& > *': {
            marginTop: theme.spacing(2),
            padding: '30px',
        },
    },
    footer: {
        marginTop: "auto !important",

    },
    book: {

    },
    contentContainer: {
        marginTop: theme.spacing(15), // Ajusta el valor según tus necesidades
    },
    GridFilter: {
        flexDirection: "row",
        display: "flex",
        justifyContent: "flex-start",
        alignItems: "center",
    },

}));


/*await axios.get(process.env.API_BASE_URL + '/api/feed/?format=json')
    .then((response) => {
        console.log(response)
    })*/

const callApi = async (category, page, setData, setCountPage, pricemin, pricemax) => {
    console.log(page, 'page')
    console.log({ pricemin, pricemax })
    let url = `http://127.0.0.1:8000/siteapp/category/${category}?page=${page}`;
    if (pricemin >= 0 && pricemax >= 0) {
        url = `${url}&pricemin=${pricemin}&pricemax=${pricemax}`;
    } else {
        url = url
    }
    console.log({ url })
    await axios.get(url,
    ).then((response) => {
        // console.log({ data: response.data })
        // console.log(response.data.length,'holaaaaaa')

        setData(response.data.results);




        // setCountPage((response.data.count / response.data.results.length).toFixed(0))
        setCountPage((response.data.count / 30).toFixed(0))
        console.log((response.data.count / response.data.results.length).toFixed(0), 'setdata')
    })
}
function formatPrice(price) {
    const formatter = new Intl.NumberFormat('es-CL', {
        style: 'currency',
        currency: 'CLP',
    });

    return formatter.format(price);
}
function textWithLimit(text, limit) {
    if (text.length <= limit) {
        return text;
    } else {
        const trimmedText = text.slice(0, limit) + '...';
        return trimmedText;
    }
}
export default function List_book_category({ category }) {
    const [data, setData] = useState([]);
    const [currentPage, setCurrentPage] = useState(1);
    const [countPage, setCountPage] = useState(1);
    const [currentCategory, setCurrentCategory] = useState(category);
    const classes = useStyles();
    useEffect(() => {
        callApi(category, currentPage, setData, setCountPage);
    }, [currentPage]);
    const handlePageChange = (event, page) => {
        setCurrentPage(page);
    };
    console.log(data, 'hola');




    const found = data.find(obj => {
        return obj.categorys;
    });
    // console.log(found, 'hola');

    return (
        (data.length) ? (
            <Grid>
                <AppBarss />



                <div className={classes.contentContainer}>
                    <Grid className={classes.book} container direction='row' justifyContent='center' >
                        {
                            found && (
                                <h1 className={classes.titlecategory}  >{found.categorys.name}</h1>

                            )
                        }


                    </Grid>
                    <Divider className={classes.divider} />
                    <Grid className={classes.GridFilter}>
                        <Grid container direction='row' justifyContent='flex-start' item md={5}>
                            <FilterCategory
                                callApi={callApi}
                                currentPage={currentPage}
                                setData={setData}
                                setCountPage={setCountPage}
                                setCurrentCategory={setCurrentCategory}
                                currentCategory={currentCategory}
                            />
                        </Grid>
                        <Grid container direction='column' justifyContent='flex-start' item md={5}>
                            <h5>Filtro Precio</h5>
                            <FilterPrice
                                callApi={callApi}
                                currentPage={currentPage}
                                setData={setData}
                                setCountPage={setCountPage}
                                currentCategory={currentCategory}

                            />
                        </Grid>
                    </Grid>






                    <Grid className={classes.root} container
                        direction="row"
                        justifyContent="center"
                        alignItems="center" item md={12}>
                        {data.map((book, key) => (

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
                                                        {textWithLimit(book.title, 25)}
                                                    </Typography>
                                                </Grid>
                                                <Grid item xs>
                                                    <Typography className={classes.category} gutterBottom variant="subtitle2">
                                                        {book.categorys.name}
                                                    </Typography>
                                                </Grid>
                                                {book.bookStore.map((bookstore, key) => (
                                                    <Grid item xs key={key} container direction='row' justifyContent='space-evenly' alignItems='baseline'>
                                                        <Typography className={classes.price} gutterBottom variant="subtitle2">
                                                            {formatPrice(bookstore.price)}
                                                        </Typography >
                                                        <Typography className={classes.store}>
                                                            {bookstore.store.name}
                                                        </Typography>
                                                    </Grid>))}

                                                {(book.calificacion) ? (
                                                    <Grid>
                                                        <Rating name="read-only" value={book.calificacion} readOnly />
                                                    </Grid>
                                                ) : (<></>)}

                                                <Grid item>
                                                    <Button className={classes.btn}>
                                                        <a href={`/view/${book.id}`} style={{ color: "white" }}>Ver Libro</a>
                                                    </Button>
                                                </Grid>
                                            </Grid>

                                        </Grid>
                                    </Grid>
                                </Paper>
                            </Grid>
                        ))}

                    </Grid>

                    <Grid container justifyContent='center' className={classes.rootPagination} item md={12}>

                        <Pagination color="primary" count={countPage} onChange={handlePageChange} />

                    </Grid>

                    <Footer className={classes.footer} />
                </div>
            </Grid>
        ) : (<></>)


    );
}