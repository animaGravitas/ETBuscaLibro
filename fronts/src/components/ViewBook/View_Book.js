import React, { useState, useEffect } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Button from '@material-ui/core/Button';
import { alpha } from '@material-ui/core/styles';
import { Grid, TextField } from '@material-ui/core';
import Card from '@material-ui/core/Card';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import Divider from '@material-ui/core/Divider';
import axios from 'axios';
import AppBar from '@material-ui/core/AppBar';
import Typography from '@material-ui/core/Typography';
import AppBarss from '../AppBar/appBar';
import PropTypes from 'prop-types';
import clsx from 'clsx';
import SwipeableViews from 'react-swipeable-views';
import { useTheme } from '@material-ui/core/styles';
import Tabs from '@material-ui/core/Tabs';
import Tab from '@material-ui/core/Tab';
import AddIcon from '@material-ui/icons/Add';
import EditIcon from '@material-ui/icons/Edit';
import UpIcon from '@material-ui/icons/KeyboardArrowUp';
import { green } from '@material-ui/core/colors';
import Box from '@material-ui/core/Box';
import Rating from '@material-ui/lab/Rating';
import Breadcrumbs from '@mui/material/Breadcrumbs';
import { Link, Stack } from '@mui/material';
import Footer from '../Footer/footer';
import NavigateNextIcon from '@material-ui/icons/NavigateNext';
import FavoriteBorderIcon from '@material-ui/icons/FavoriteBorder';
import FavoriteIcon from '@material-ui/icons/Favorite';


function TabPanel(props) {
    const { children, value, index, ...other } = props;

    return (
        <Typography
            component="div"
            role="tabpanel"
            hidden={value !== index}
            id={`action-tabpanel-${index}`}
            aria-labelledby={`action-tab-${index}`}
            {...other}
        >
            {value === index && <Box p={3}>{children}</Box>}
        </Typography>
    );
}

TabPanel.propTypes = {
    children: PropTypes.node,
    index: PropTypes.any.isRequired,
    value: PropTypes.any.isRequired,
};

function a11yProps(index) {
    return {
        id: `action-tab-${index}`,
        'aria-controls': `action-tabpanel-${index}`,
    };
}

const useStyles = makeStyles((theme) => ({
    root: {
        flexGrow: 1,


    },
    menuButton: {
        marginRight: theme.spacing(2),
    },
    title: {
        flexGrow: 0.9,
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
    inputInput: {
        padding: theme.spacing(1, 1, 1, 0),
        // vertical padding + font size from searchIcon
        paddingLeft: `calc(1em + ${theme.spacing(4)}px)`,
        transition: theme.transitions.create('width'),
        width: '100%',
        [theme.breakpoints.up('md')]: {
            width: '20ch',
        },
    },
    book: {
        marginTop: '33px',

    },

    card: {
        border: 'inset',
        height: '493px'
    },
    bullet: {
        display: 'inline-block',
        margin: '0 2px',
        transform: 'scale(0.8)',
    },
    title: {
        fontSize: 14,
    },
    pos: {
        marginBottom: 12,
    },
    img: {
        width: '70%',
        height: '80%',
    },
    list: {
        justifyContent: 'space-between',
        padding: "36px",

    },
    btn: {
        backgroundColor: '#3f51b5',
        color: '#fff',
        "&:hover": {
            color: "#",
            backgroundColor: 'blue',
        }
    },
    img_logo: {
        width: '20%',
        height: '20%'
    },
    fab: {
        position: 'absolute',
        bottom: theme.spacing(2),
        right: theme.spacing(2),
    },
    fabGreen: {
        color: theme.palette.common.white,
        backgroundColor: green[500],
        '&:hover': {
            backgroundColor: green[600],
        },
    },
    img_comment: {
        width: '80px',
        height: '80px',
        borderRadius: '50%', 
        objectFit: 'cover',
    },
    discount: {

    },
    titleBook: {
        fontSize: "20px",
        width: "90%",
    },
    contentContainer: {
        marginTop: theme.spacing(-1),
    },
    contentContainerFiltro: {
        marginTop: theme.spacing(10), 
    },
    commentContainer: {
        marginBottom: theme.spacing(2),
        padding: theme.spacing(2),
        border: `1px solid ${theme.palette.grey[300]}`,
        borderRadius: theme.spacing(1),
      },
    username: {
        fontWeight: 'bold',
        marginBottom: theme.spacing(1),
    },
    rating: {
        color: theme.palette.primary.main,
        marginBottom: theme.spacing(1),
    },
    commentText: {
        marginBottom: theme.spacing(1),
    },
    updateButton: {
        marginRight: theme.spacing(1),
      },
    deleteButton: {
        marginLeft: theme.spacing(1),
    },
}));



export default function ViewBook({ bookId }) {
    const [isFavorite, setIsFavorite] = useState(false);
    const [iconName, setIconName] = useState('FavoriteBorderIcon');
    const classes = useStyles();
    const [data, setData] = useState({});
    const [comment, setComment] = useState('');
    const [rating, setRating] = useState(0);
    const [comments, setComments] = useState([]);
    const [selectedComment, setSelectedComment] = useState('');
    const [selectedCommentId, setSelectedCommentId] = useState(null);
    const [selectedRating, setSelectedRating] = useState(null);
    const [editedComments, setEditedComments] = useState({});
    const [isEditing, setIsEditing] = useState(false);
    const username = localStorage.getItem('username');
    useEffect(() => {

        const callApi = async () => {
            await axios.get(`http://127.0.0.1:8000/siteapp/book-detail/${bookId}?format=json`,

            ).then((response) => {
                console.log({ data: response.data })
                console.log('holaaaaaa')

                setData(response.data)
            })

        }
        callApi();
    }, []);
    const theme = useTheme();
    const [value, setValue] = React.useState(0);


    const handleChange = (event, newValue) => {
        setValue(newValue);
    };

    const handleChangeIndex = (index) => {
        setValue(index);
    };

    const transitionDuration = {
        enter: theme.transitions.duration.enteringScreen,
        exit: theme.transitions.duration.leavingScreen,
    };
    function handleClick(event) {
        event.preventDefault();
        console.info('You clicked a breadcrumb.');
    }

    const fabs = [
        {
            color: 'primary',
            className: classes.fab,
            icon: <AddIcon />,
            label: 'Add',
        },
        {
            color: 'secondary',
            className: classes.fab,
            icon: <EditIcon />,
            label: 'Edit',
        },
        {
            color: 'inherit',
            className: clsx(classes.fab, classes.fabGreen),
            icon: <UpIcon />,
            label: 'Expand',
        },
    ];
    const save_id = bookId;

    useEffect(() => {
        const username = localStorage.getItem('username');
      
        const checkFavoriteStatus = async () => {
          try {
            const response = await axios.get(`http://127.0.0.1:8000/siteapp/check-favorite/${username}/${bookId}`);
            const { isFavorite } = response.data;
      
            setIsFavorite(isFavorite);
      
            if (isFavorite) {
              setIconName('FavoriteIcon');
            } else {
              setIconName('FavoriteBorderIcon');
            }
          } catch (error) {
            console.error('Error al verificar el estado del favorito:', error);
          }
        };
      
        checkFavoriteStatus();
    }, [bookId]);
      
    const handleClickFavorite = async () => {
        const newIsFavorite = !isFavorite;
        const icon = newIsFavorite ? 'FavoriteIcon' : 'FavoriteBorderIcon';
        setIconName(icon);
        setIsFavorite(newIsFavorite);
      
        const username = localStorage.getItem('username');
      
        try {
          await axios.post('http://127.0.0.1:8000/siteapp/favorite/', {
            bookId: save_id,
            isFavorite: newIsFavorite,
            username: username,
          });
      
          console.log('Solicitud enviada correctamente al backend');
        } catch (error) {
          console.error('Error al enviar la solicitud al backend:', error);
        }
    };

    const handleCommentChange = (commentId, value) => {
        setEditedComments((prevEditedComments) => ({
          ...prevEditedComments,
          [commentId]: {
            ...prevEditedComments[commentId],
            comentario: value,
          },
        }));
      };
      
    
      const handleRatingChange = (commentId, value) => {
        setEditedComments((prevEditedComments) => ({
          ...prevEditedComments,
          [commentId]: {
            ...prevEditedComments[commentId],
            calificacion: value,
          },
        }));
        setSelectedRating(value); // Agrega esta línea para reflejar el cambio en el rating seleccionado
      };
    
    const fetchComments = async () => {
        try {
          const response = await axios.get(`http://127.0.0.1:8000/siteapp/comments/${bookId}`);
          setComments(response.data);
        } catch (error) {
          console.error('Error al obtener los comentarios:', error);
        }
      };
      
      useEffect(() => {
        fetchComments(); // Llamar a la función fetchComments al cargar el componente
    }, [bookId]);

    const handleRatingChangeNewComment = (event, value) => {
        setRating(value);
      };
      
      const handleCommentChangeNewComment = (event) => {
        setComment(event.target.value);
      };
      
    const handleCommentSubmit = async (event) => {
        event.preventDefault();
        
        const username = localStorage.getItem('username');
        
        try {
            await axios.post('http://127.0.0.1:8000/siteapp/comment-create/', {
            bookId: save_id,
            username: username,
            rating: rating,
            comment: comment,
            });
        
            console.log('Comentario enviado correctamente al backend');
            fetchComments();
        
            setComment('');
            setRating(0);
        } catch (error) {
            console.error('Error al enviar el comentario al backend:', error);
        }
    };

    const handleCommentUpdate = async (commentId) => {
        const updatedComment = {
          ...comments.find((comment) => comment.comment_id === commentId),
          comentario: editedComments[commentId].comentario,
          calificacion: editedComments[commentId].calificacion,
        };
      
        try {
          await axios.put(`http://127.0.0.1:8000/siteapp/comment-update/${commentId}/`, updatedComment);
      
          console.log('Comentario actualizado correctamente');
          fetchComments();
          handleCancelEdit();
        } catch (error) {
          console.error('Error al actualizar el comentario:', error);
        }
      
        setSelectedComment(null);
    };
      
    
      const handleEditComment = (comment) => {
        setSelectedCommentId(comment.comment_id);
        setEditedComments((prevEditedComments) => ({
          ...prevEditedComments,
          [comment.comment_id]: {
            comentario: comment.comentario,
            calificacion: comment.calificacion,
          },
        }));
        setSelectedRating(comment.calificacion);
        setIsEditing(true); 
      };

      const handleCancelEdit = () => {
        setIsEditing(false);
        setSelectedCommentId(null);
        setSelectedRating(null);
        setEditedComments({});
      };

    const handleCommentDelete = async (commentId) => {
        try {
            await axios.delete(`http://127.0.0.1:8000/siteapp/comment-delete/${commentId}/`);

            console.log('Comentario eliminado correctamente');
            fetchComments();
        } catch (error) {
            console.error('Error al eliminar el comentario:', error);
        }
    };

      
    return (
        <>
            <AppBarss></AppBarss>
            <div className={classes.contentContainer}>
                <Grid justifyContent='flex-start' style={{ paddingLeft: "108px", paddingTop: "22px" }} container item md={10}>
                    <div role="presentation" onClick={handleClick}>
                        <div className={classes.contentContainerFiltro}>
                            <Breadcrumbs aria-label="breadcrumb" separator={<NavigateNextIcon />}>
                                <Link underline="hover" color="inherit" href="/home">
                                    Home
                                </Link>

                                {data && data.categorys && data.categorys.map((category, key) => (

                                    <Stack>
                                        <Link underline="hover"
                                            color="inherit"
                                            href={`/category/${category.id}`}>
                                            {category.name}

                                        </Link>
                                    </Stack>



                                ))}
                                <Typography className={classes.title} color="text.primary">{data.title}</Typography>
                            </Breadcrumbs>
                        </div>
                    </div>
                </Grid>
                <Grid className={classes.root} container
                    direction="row"
                    justifyContent="center"
                    alignItems="center" item md={12}>
                    <Grid className={classes.book} item md={10}>
                        <Card className={clsx(classes.card, classes.contentContainer)} item md={12}>
                            <CardContent container item md={12}>
                                <Grid container direction='row'>
                                    <Grid item md={6}>
                                        <img className={classes.img} src={data.image} />
                                    </Grid>
                                    <Grid direction='column' item md={6}>
                                        <Grid container justifyContent='space-between'>
                                            <h1 className={classes.titleBook}>{data.title}</h1>
                                            {localStorage.getItem('authenticated') === 'true' ? (
                                                iconName === 'FavoriteBorderIcon' ? (
                                                    <FavoriteBorderIcon fontSize='large' onClick={() => handleClickFavorite(true)} />
                                                ) : (
                                                    <FavoriteIcon fontSize='large' onClick={() => handleClickFavorite(false)} />
                                                )
                                            ) : null}
                                        </Grid>
                                        <Typography className={classes.category} gutterBottom variant="subtitle2">
                                            <h3>autor: {data.autor}</h3>
                                        </Typography>
                                        <Typography className={classes.category} gutterBottom variant="subtitle2">
                                            <h4>editorial: {data.editorial}</h4>
                                        </Typography>
                                        <Typography className={classes.category} gutterBottom variant="subtitle2">
                                            <h5>isbn: {data.isbn}</h5>
                                        </Typography>

                                        {(data.calificacion) ? (
                                            <Grid>
                                                <Rating name="read-only" value={data.calificacion} readOnly />
                                            </Grid>
                                        ) : (<></>)}

                                        <Grid>
                                            <List component="nav" className={classes.root} aria-label="mailbox folders">
                                                {data && data.stores && data.stores.map((store, key) => (
                                                    <>
                                                        <ListItem key={key} className={classes.list} button>
                                                            <img className={classes.img_logo} src={store.image} />
                                                            {(store.discount) ? (<h5 className={classes.discount}>{store.discount}</h5>
                                                            ) : (<></>)}
                                                            <Button className={classes.btn}><a href={store.url_book} style={{color:"white"}} target="_blank">${store.price}</a></Button>
                                                        </ListItem>
                                                        <Divider />
                                                    </>
                                                ))}
                                            </List >
                                        </Grid>
                                    </Grid>
                                </Grid>


                            </CardContent>
                            <CardActions>
                            </CardActions>
                        </Card>
                        <Grid className={classes.book} item md={12}>
                            <Grid className={classes.root} item md={12}>
                                <AppBar position="static" color="default">
                                    <Tabs
                                        value={value}
                                        onChange={handleChange}
                                        indicatorColor="primary"
                                        textColor="primary"
                                        variant="fullWidth"
                                        aria-label="action tabs example"
                                    >
                                        <Tab label="Reseña" {...a11yProps(0)} />
                                        <Tab label="Especificaciones" {...a11yProps(1)} />
                                    </Tabs>
                                </AppBar>
                                <SwipeableViews
                                    axis={theme.direction === 'rtl' ? 'x-reverse' : 'x'}
                                    index={value}
                                    onChangeIndex={handleChangeIndex}
                                >
                                    <TabPanel value={value} index={0} dir={theme.direction}>
                                        <p>{data.reseña}</p>
                                    </TabPanel>
                                    <TabPanel value={value} index={1} dir={theme.direction}>
                                        <p>categoria: {data.category}</p>
                                        <p>sub categoria: {data.sub_category}</p>
                                        <p>formato: {data.formato}</p>
                                        <p>idioma: {data.idioma}</p>
                                        <p>pagina: {data.pagina}</p>
                                    </TabPanel>
                                </SwipeableViews>

                            </Grid>
                            <Grid className={classes.root} item md={12}>
                                <List component="nav" className={classes.root} aria-label="mailbox folders" item md={12}>
                                    {(data?.comments?.length) ? (<h1>Comentarios del libro</h1>
                                    ) : (<></>)}
                                    {data?.comments?.map((comment, key) => (

                                        <>
                                            <ListItem key={key} className={classes.list} item md={12}>
                                                <img className={classes.img_comment} src={comment.image} />
                                                <Grid item md={11} >
                                                    <Grid item md={12}>
                                                        <span item md={6}>{comment.name}</span>
                                                        <Rating item md={6} style={{ position: 'absolute' }} name="read-only" value={comment.rating} readOnly />

                                                    </Grid>
                                                    <Grid item md={12} style={{ marginTop: '21px' }} >
                                                        <span>{comment.description}</span>
                                                    </Grid>
                                                </Grid>
                                            </ListItem>


                                            <Divider />
                                        </>
                                    ))}
                                </List>
                            </Grid>
                            <Grid className={classes.root} item md={12}>
                                <List component="nav" className={classes.root} aria-label="mailbox folders" item md={12}>
                                {comments.map((comment, key) => (
                                    <React.Fragment key={key}>
                                    <ListItem className={classes.list} item md={12}>
                                        <img className={classes.img_comment} src={comment.user_image} />
                                        <Grid item md={11}>
                                        <Grid item md={12}>
                                            <span item md={6}>{comment.username}</span>
                                            {selectedCommentId === comment.comment_id && isEditing ? (
                                            <Grid item md={6}>
                                                <Rating
                                                name={`rating-${comment.comment_id}`}
                                                value={selectedRating}
                                                onChange={(event, newValue) => handleRatingChange(comment.comment_id, newValue)}
                                                />
                                            </Grid>
                                            ) : (
                                            <Rating
                                                style={{ position: 'absolute' }}
                                                name="read-only"
                                                value={comment.calificacion}
                                                readOnly
                                            />
                                            )}
                                        </Grid>
                                        <Grid item md={12} style={{ marginTop: '21px' }}>
                                            {selectedCommentId === comment.comment_id && isEditing ? (
                                            <TextField
                                                id={`comment-${comment.comment_id}`}
                                                label="Comentario"
                                                multiline
                                                rows={4}
                                                value={selectedCommentId === comment.comment_id ? editedComments[comment.comment_id].comentario : comment.comentario}
                                                onChange={(event) => handleCommentChange(comment.comment_id, event.target.value)}
                                                variant="outlined"
                                                fullWidth
                                            />
                                            ) : (
                                            <span>{comment.comentario}</span>
                                            )}
                                        </Grid>
                                        {comment.username === username && (
                                            <Grid item md={12}>
                                            {selectedCommentId === comment.comment_id && isEditing ? (
                                                <React.Fragment>
                                                <Button
                                                    variant="contained"
                                                    color="primary"
                                                    onClick={() => handleCommentUpdate(comment.comment_id)}
                                                >
                                                    Actualizar
                                                </Button>
                                                <Button
                                                    variant="contained"
                                                    color="secondary"
                                                    onClick={handleCancelEdit}
                                                >
                                                    Cancelar
                                                </Button>
                                                </React.Fragment>
                                            ) : (
                                                <Button
                                                variant="contained"
                                                color="primary"
                                                onClick={() => handleEditComment(comment)}
                                                >
                                                Editar
                                                </Button>
                                            )}
                                            <Button
                                                variant="contained"
                                                color="secondary"
                                                onClick={() => handleCommentDelete(comment.comment_id)}
                                            >
                                                Eliminar
                                            </Button>
                                            </Grid>
                                        )}
                                        </Grid>
                                    </ListItem>
                                    <Divider />
                                    </React.Fragment>
                                ))}
                                </List>
                            </Grid>
                            
                            {localStorage.getItem('authenticated') === 'true' ? (
                                <form onSubmit={handleCommentSubmit}>
                                    <div>
                                        <Typography variant="h6">Deja un comentario</Typography>
                                    </div>
                                    <div>
                                        <Rating name="rating" value={rating} onChange={handleRatingChangeNewComment} />
                                    </div>
                                    <div>
                                        <TextField
                                        id="comment"
                                        label="Comentario"
                                        multiline
                                        rows={4}
                                        value={comment}
                                        onChange={handleCommentChangeNewComment}
                                        variant="outlined"
                                        fullWidth
                                        />
                                    </div>
                                    <div>
                                        <Button variant="contained" color="primary" type="submit">
                                        Enviar comentario
                                        </Button>
                                    </div>
                                </form>
                            ) : null}
                        </Grid>
                    </Grid>
                    <Grid item md={12} style={{ marginTop: '70px' }} >
                    </Grid>
                    <Footer />
                </Grid>
            </div>    
        </>

    );

}
