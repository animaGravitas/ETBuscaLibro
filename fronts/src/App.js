import React from 'react';
import Home from './components/Home';
import { Router } from "@reach/router"
import ViewBook from './components/ViewBook/View_Book';
import InitialPage from './components/Home/initial_page';
import List_book from './components/ViewBook/List_book';
import List_book_category from './components/ViewBook/List_book_category';
import Search from './components/Search/Search.js';



export default function App() {
  return (
    <Router>
      <List_book path="/list_book"  />
      <ViewBook path="/view/:bookId" />
      
      {/* <InitialPage path="/chao/" /> */}
      
      <Home path="/" />
      <Search path="buscar"/>
      <List_book_category path="/category/:category"/>
    </Router>
  );
}
