import React, { useState, useEffect } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import AppBarss from '../AppBar/appBar';



const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
  },
}));



export default function Search() {
  const classes = useStyles();
  const [searchQuery, setSearchQuery] = useState('');
  const [books, setBooks] = useState([]);
  const [inputValue, setInputValue] = useState('');




  const handleSubmit = (event) => {
    const callApi = async (inputValue) => {
      await axios.get(`http://127.0.0.1:8000/siteapp/search/?search=${inputValue}`,
      ).then((response) => {
        // console.log({ data: response.data })

        setBooks(response.data.books);
        console.log(books, 'books')
      })
    }
    event.preventDefault();
    console.log('Valor guardado:', inputValue);
    callApi(inputValue);
  };
  const handleChange = (event) => {
    setInputValue(event.target.value);
  

  };
  return (
    <>
    <AppBarss/>
    <div>
      <form >
        <input type="text" value={inputValue} onChange={handleChange} />
        <button type="button" onClick={handleSubmit} >Guardar</button>
      </form>
    </div>
    </>
    
  );

};