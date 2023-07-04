import React, { useState, useEffect } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Carousel from '../../components/carousel/Carousel';
import { Grid } from '@material-ui/core';




const useStyles = makeStyles((theme) => ({
    root: {
        flexGrow: 1,
        overflowX: "hidden",
    },
    carousel: {
        //backgroundColor: 'red',
        textAlign: '-webkit-center',

    },
    grid: {
        width: "1000px",
        textAlign: "-webkit-center",
    },




}));


export default function InitialPage() {
    const [dataNovedades, setnovedades] = useState([]);
    const [dataVendidos, setVendido] = useState([]);
    const [dataMundoComic, setDtaMundoComic] = useState([]);
    const [dataComputacionInformatica, setComputacionInformatica] = useState([]);
    const [dataLiteratura, setLiteratura] = useState([]);
    const [dataInfatil, setInfatil] = useState([]);
    const [dataCiencias, setCiencias] = useState([]);






    const classes = useStyles();


    useEffect(() => {
        const fetchData = async () => {
            try {
                const response5 = await fetch('http://127.0.0.1:8000/siteapp/category-novedades/?format=json');
                const dataNovedades = await response5.json();
                setnovedades(dataNovedades);

                const response6 = await fetch('http://127.0.0.1:8000/siteapp/category-vendidos/?format=json');
                const dataVendidos = await response6.json();
                setVendido(dataVendidos);

                const response1 = await fetch('http://127.0.0.1:8000/siteapp/category-mundo-Comic/?format=json');
                const dataMundoComic = await response1.json();
                setDtaMundoComic(dataMundoComic);

                const response2 = await fetch('http://127.0.0.1:8000/siteapp/category-computacion-informatica/?format=json');
                const dataComputacionInformatica = await response2.json();
                setComputacionInformatica(dataComputacionInformatica);

                const response3 = await fetch('http://127.0.0.1:8000/siteapp/category-literatura/?format=json');
                const dataLiteratura = await response3.json();
                setLiteratura(dataLiteratura);


                const response4 = await fetch('http://127.0.0.1:8000/siteapp/category-infantil/?format=json');
                const dataInfatil = await response4.json();
                setInfatil(dataInfatil);

                const response7 = await fetch('http://127.0.0.1:8000/siteapp/category-ciencias/?format=json');
                const dataCiencias = await response7.json();
                setCiencias(dataCiencias);




                // Procesar los datos recibidos si es necesario
            } catch (error) {
                throw error;
                console.error('Error:', error);
            }
        };

        fetchData();
    }, []);
    console.log(dataMundoComic, 'datas mundo');
    // console.log(dataComputacionInformatica, 'data informatica');

    const listCategoriesRow = [dataNovedades, dataVendidos];
    const listCategoriesColumn = [dataCiencias, dataMundoComic];


    return (
        <>
            <Grid container direction='row' >
                {listCategoriesRow.map((category) => (
                    (category.length) ? (


                        <Grid className={classes.carousel} item xs={12} md={6} justifyContent="center">
                            <h1 className={classes.title}>{category[0].categorys.name}</h1>

                            <Carousel
                                className={classes.carouselCarousel}
                                listData={category}
                            />

                        </Grid>

                    ) : (<>
                    </>)
                ))}
            </Grid >
            <Grid container direction='column'  style={{marginBottom:"30px"}}>
                {listCategoriesColumn.map((category) => (
                    (category.length) ? (


                        <Grid className={classes.carousel} item xs={12} justifyContent="center">
                            <h1 className={classes.title}>{category[0].categorys.name}</h1>

                            <Carousel
                                listData={category}
                            />

                        </Grid>

                    ) : (<></>)
                ))}
            </Grid >

        </>

    );

}