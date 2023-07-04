import React from 'react';
import Item from './Item';
import Carousel from 'react-material-ui-carousel';
import { makeStyles } from '@material-ui/core/styles';

const useStyles = makeStyles((theme) => ({
    grid: {
        textAlign: "-webkit-center",
    },
}));

function CarouselCustom({ listData }) {
    const classes = useStyles();
    console.log(listData, 'listbook;Carousel')
    return (
        <Carousel
            interval={3000}
            animation='fade'
            duration={100}
            indicators={true}
            stopAutoPlayOnHover
            item md={12}
            alignItems='center'
            className={classes.grid}
            autoPlay={false}
        >
            {
                listData.map(item => <Item key={item.id} item={item} />)
            }
        </Carousel>
    )
}

export default CarouselCustom