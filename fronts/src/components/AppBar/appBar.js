import React, { useState, useEffect } from 'react';
import { makeStyles,  } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';
import IconButton from '@material-ui/core/IconButton';
import MenuIcon from '@material-ui/icons/Menu';
import SearchIcon from '@material-ui/icons/Search';
import { alpha } from '@material-ui/core/styles';
import InputBase from '@material-ui/core/InputBase';
import Grid from '@material-ui/core/Grid';
import Menu from '@material-ui/core/Menu';
import MenuItem from '@material-ui/core/MenuItem';
import HomeIcon from '@material-ui/icons/Home';
import { Hidden } from '@material-ui/core';
import axios from 'axios';
import { Avatar } from '@material-ui/core';
import { createTheme, ThemeProvider } from '@material-ui/core/styles';
import clsx from 'clsx';

const theme = createTheme();

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
  },
  menuButton: {
    marginRight: theme.spacing(2),
  },
  title: {
    flexGrow: 1,
    textAlign: 'center',
    [theme.breakpoints.up('sm')]: {
      textAlign: 'left',
    },
  },
  search: {
    position: 'relative',
    borderRadius: theme.shape.borderRadius,
    backgroundColor: alpha(theme.palette.common.white, 0.15),
    '&:hover': {
      backgroundColor: alpha(theme.palette.common.white, 0.25),
    },
    marginLeft: 'auto',
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
  inputInput: {
    padding: theme.spacing(1, 1, 1, 0),
    paddingLeft: `calc(1em + ${theme.spacing(4)}px)`,
    transition: theme.transitions.create('width'),
    width: '100%',
    [theme.breakpoints.up('md')]: {
      width: '20ch',
    },
  },
  link: {
    textDecoration: 'none',
    color: theme.palette.common.white,
    '&:hover': {
      color: theme.palette.common.white,
    },
  },
  buttonContainer: {
    marginLeft: theme.spacing(15),
  },

  btnBusqueda: {
    color: theme.palette.common.white,
    '&:hover': {
      color: theme.palette.common.white,
    },
  },

  menuButton: {
    color: theme.palette.common.white,
  },
  menuButtonColor: {
    color: theme.palette.common.white,
  },
  menuItem: {
    '& .MuiMenuItem-root': {
      backgroundColor: theme.palette.primary.main,
    },
  },
}));


export default function AppBarss() {
  const [searchTerm, setSearchTerm] = useState('');
  const classes = useStyles();
  const params = new URLSearchParams(window.location.search);
  let authenticated = localStorage.getItem('authenticated') || '';
  let username = localStorage.getItem('username') || '';
  const [anchorEl, setAnchorEl] = React.useState(null);
  const [searchQuery, setSearchQuery] = useState('');
  const [books, setBooks] = useState([]);
  const [inputValue, setInputValue] = useState('');
  const [showResults, setShowResults] = useState(false);

  if (params.has('authenticated')) {
    authenticated = params.get('authenticated');
    localStorage.setItem('authenticated', authenticated);
  }

  if (params.has('username')) {
    username = params.get('username');
    localStorage.setItem('username', username);
  }

  const handleChange = (event) => {
    setInputValue(event.target.value);


  };

  const handleSubmit = (event) => {
      event.preventDefault();
      // Aquí puedes hacer algo con el valor guardado, como enviarlo a una API o procesarlo de alguna manera.
      console.log('Valor guardado:', inputValue);
      window.location = `/list_book/?search=${inputValue}`;
  };
  
  const renderProfileLink = () => {
    if (authenticated === 'true') {
      return (
        <div className={classes.buttonContainer}>
          <Typography variant="body2" style={{ marginRight: '10px', color: theme.palette.common.white }}>
            Bienvenido, {username}
          </Typography>
          <Button className={classes.btnicon}>
            <a href={`http://127.0.0.1:8000/users/profile/${username}`} className={classes.link}>
              <Avatar alt={username} src="../assests/imglogo/PerfilIcon.png" /> 
            </a>
          </Button>
          <Button className={classes.btnicon}>
            <a href="http://127.0.0.1:8000/main/" className={classes.link}>
              Publicaciones
            </a>
          </Button>
          <Button className={classes.btnicon}>
            <a href="http://127.0.0.1:8000/siteapp/favorite-books" className={classes.link}>
              Favoritos
            </a>
          </Button>
          <Button className={classes.btnicon}>
            <a href="http://127.0.0.1:8000/users/logout" className={classes.link}>
              Salir
            </a>
          </Button>
        </div>
      );
    } else {
      return (
        <div className={classes.buttonContainer}>
          <Button className={classes.btnicon}>
            <a href="http://127.0.0.1:8000/main/" className={classes.link}>
              Publicaciones
            </a>
          </Button>
          <Button className={classes.btnicon}>
            <a href="http://127.0.0.1:8000/users/login" className={classes.link}>
              Iniciar sesión
            </a>
          </Button>
          <Button className={classes.btnicon}>
            <a href="http://127.0.0.1:8000/users/register" className={classes.link}>
              Registrarse
            </a>
          </Button>
        </div>
      );
    }
  };

  const renderMenuItems = () => {
    if (authenticated === 'true') {
      return (
        <div className={classes.menuItem}>
          <MenuItem>
            <a href={`http://127.0.0.1:8000/users/profile/${username}`} className={classes.link}>
              Perfil
            </a>
          </MenuItem>
          <MenuItem>
            <a href="http://127.0.0.1:8000/main/" className={classes.link}>
              Publicaciones
            </a>
          </MenuItem>
          <MenuItem>
            <a href="http://127.0.0.1:8000/siteapp/favorite-books" className={classes.link}>
              Favoritos
            </a>
          </MenuItem>
          <MenuItem>
            <a href="http://127.0.0.1:8000/users/logout" className={classes.link}>
              Salir
            </a>
          </MenuItem>
        </div>
      );
    } else {
      return (
        <div className={classes.menuItem}>
          <MenuItem>
            <a href="http://127.0.0.1:8000/main/" className={classes.link}>
              Publicaciones
            </a>
          </MenuItem>
          <MenuItem>
            <a href="http://127.0.0.1:8000/users/login" className={classes.link}>
              Iniciar sesión
            </a>
          </MenuItem>
          <MenuItem>
            <a href="http://127.0.0.1:8000/users/register" className={classes.link}>
              Registrarse
            </a>
          </MenuItem>
        </div>
      );
    }
  };


  return (
    <div className={classes.root}>
      <AppBar position="fixed"> 
        <Toolbar>
          <Typography variant="h6" className={classes.title}>
            <a href="/" className={classes.link}>
              BuscaLibro
            </a>
          </Typography>
          <Hidden mdUp>
          <Grid className={classes.search} item md={4}>
              <Grid className={classes.searchIcon}>
                <SearchIcon />
              </Grid>
              <Grid>
                <InputBase
                  type="text"
                  value={inputValue}
                  onChange={handleChange}
                  classes={{
                    root: classes.inputRoot,
                    input: classes.inputInput,
                  }}
                  inputProps={{ 'aria-label': 'search' }}
                />
              </Grid>
            </Grid>
            <Grid item md={3} container justifyContent='flex-start'>
              <Button className={classes.btnBusqueda} type="submit" onClick={handleSubmit}>
                Buscar
              </Button>
            </Grid>
            <IconButton
              edge="start"
              className={clsx(classes.menuButton, classes.menuButtonColor)} // Aplica ambas clases al botón del menú
              aria-label="menu"
              onClick={(event) => setAnchorEl(event.currentTarget)}
            >
              <MenuIcon />
            </IconButton>
            <Menu
              id="menu-appbar"
              anchorEl={anchorEl}
              keepMounted
              open={Boolean(anchorEl)}
              onClose={() => setAnchorEl(null)}
              classes={{ paper: classes.menuItem }} // Aplica la clase de estilo personalizado al menú desplegable
            >
              {renderMenuItems()}
            </Menu>
          </Hidden>
          <Hidden smDown>
            <Grid className={classes.search} item md={4}>
              <Grid className={classes.searchIcon}>
                <SearchIcon />
              </Grid>
              <Grid>
                <InputBase
                  type="text"
                  value={inputValue}
                  onChange={handleChange}
                  classes={{
                    root: classes.inputRoot,
                    input: classes.inputInput,
                  }}
                  inputProps={{ 'aria-label': 'search' }}
                />
              </Grid>
            </Grid>
            <Grid item md={3} container justifyContent='flex-start'>
              <Button className={classes.btnBusqueda} type="submit" onClick={handleSubmit}>
                Buscar
              </Button>
            </Grid>
            <div>{renderProfileLink()}</div>
          </Hidden>
        </Toolbar>
      </AppBar>
    </div>
  );
}
