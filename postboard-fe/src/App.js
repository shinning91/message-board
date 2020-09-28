import React, { Component } from 'react';
import axios from 'axios';
import logo from './logo.svg';
import './App.css';

axios.defaults.headers.common['Content-Type'] = 'application/json';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      posts: [],
      comments: [],
      keyword: ''
    }
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }
  componentDidMount() {
    axios.get('/board/')
    .then(res => {
        const posts = res.data['posts'];
        this.setState({ posts });
    })
  }
  handleChange(event) {
    this.setState({keyword: event.target.value});
  }
  handleSubmit(event) {
    console.log(this.state.keyword);
    axios.post('/search/', {'keyword': this.state.keyword}
    ).then(res => {
        const comments = res.data['comments'];
        this.setState({ comments });
    })
    event.preventDefault();
  }
  renderPosts = () => {
    const newPosts = this.state.posts;
    return newPosts.map(item => (
      <li key={item.post_id} className="list-group-item d-flex justify-content-between align-items-center">
        <div>
          <h1>{item.post_title}</h1>
          {item.post_body}
          <div>
            Comment(s): {item.total_number_of_comments}
          </div>
        </div>
      </li>
    ));
  };
  renderComments = () => {
    const newComments = this.state.comments;
    return newComments.map(item => (
      <li key={item.id} className="list-group-item d-flex justify-content-between align-items-center">
        <div>
          <h1>Post ID: {item.postId}</h1>
          <p>Name: {item.name}</p>
          <p>Email: {item.email}</p>
          {item.body}
        </div>
      </li>
    ));
  };
  render() {
    let content;
    if (this.state.comments && this.state.comments.length > 0) {
      content = this.renderComments()
    } else {
      content = this.renderPosts()
    }
    return (
      <main className="content">
        <h1 className="text-white text-uppercase text-center my-4">Board Post</h1>
        <div className="row">
          <div className="col-md-6 col-sm-10 mx-auto p-0">
            <div>
            <form onSubmit={this.handleSubmit}>
              <label className='text-white'>
                Search comment : 
                <input type="text" name="serch" value={this.state.value} onChange={this.handleChange}/>
              </label>
              <input type = "submit" value = "Submit"/>
            </form>
            </div>
            <ul className="list-group list-group-flush">
              {content}
            </ul>
          </div>
        </div>
      </main>
    )
  } 
}

export default App;
