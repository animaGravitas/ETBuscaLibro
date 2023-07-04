import React, { useState, useEffect } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';
import IconButton from '@material-ui/core/IconButton';
import MenuIcon from '@material-ui/icons/Menu';
import SearchIcon from '@material-ui/icons/Search';
import { alpha } from '@material-ui/core/styles';
import InputBase from '@material-ui/core/InputBase';
import { Grid } from '@material-ui/core';
/*import Book from './../ViewBook/book';*/
import axios from 'axios';
import AppBarss from '../AppBar/appBar';
import List_book from '../ViewBook/List_book';
import InitialPage from './initial_page';
import Divider from '@material-ui/core/Divider';
import Footer from '../Footer/footer';
import List_book_category from '../ViewBook/List_book_category';


const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,

  },
  divider: {
    margin: '35px',
  },
  title: {
    textAlign: 'center',
  },
  search: {
    position: 'relative',
    borderRadius: theme.shape.borderRadius,
    backgroundColor: alpha(theme.palette.common.white, 0.15),
    '&:hover': {
      backgroundColor: alpha(theme.palette.common.white, 0.25),
    },
    marginRight: theme.spacing(4),
    width: '30%',

  },
  searchIcon: {
    padding: theme.spacing(0, 2),
    height: '100%',
    position: 'absolute',
    pointerEvents: 'none',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
  },
  inputRoot: {
    color: 'inherit',
  },
  contentContainer: {
    marginTop: theme.spacing(15),
  },
  contentContainerFooter: {
    marginTop: theme.spacing(15), 
  },
}));




export default function Home() {
  const [data, setData] = useState([]);
  const classes = useStyles();

  return (
    <div className={classes.root}>
      <AppBarss
      />
        <div className={classes.contentContainer}>
          <InitialPage
          />
        </div>
        <div className={classes.contentContainerFooter}>  
          <Footer />
        </div>
    </div>

  );

}




