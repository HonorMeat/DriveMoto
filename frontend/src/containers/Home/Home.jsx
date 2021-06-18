import React, { Component } from 'react'
import axios from 'axios'

import './Home.sass'

import c1 from './img/c1.png'
import c2 from './img/c2.png'
import c3 from './img/c3.png'
import c4 from './img/c4.png'
import c5 from './img/c5.png'
import c6 from './img/c6.png'

import add from './img/add.png'
import slider from './img/slider.jpg'

import SliderUI from '../../components/UI/Slider/Slider'

import { NavLink } from 'react-router-dom'


function CustomNextArrow(props){
  const { className, style, onClick } = props
  return(
    <div className={ className } style={{...style}} onClick={ onClick }>
        <svg width="17" height="29" viewBox="0 0 17 29" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M15.8936 13.632L2.33608 0.236548C2.01686 -0.0788495 1.50491 -0.0788495 1.1857 0.236548C0.866485 0.551946 0.866485 1.05777 1.1857 1.37317L14.1651 14.1974L1.1857 27.0216C0.866485 27.337 0.866485 27.8428 1.1857 28.1582C1.3423 28.3129 1.5531 28.3962 1.75788 28.3962C1.96266 28.3962 2.17346 28.3189 2.33005 28.1582L15.8876 14.7627C16.2068 14.4533 16.2068 13.9415 15.8936 13.632Z" fill="white"/>
        </svg>
    </div>
  )
}

function CustomPrevArrow(props){
  const { className, style, onClick } = props
  return(
    <div className={ className } style={{...style}} onClick={ onClick }>
      <svg width="16" height="29" viewBox="0 0 16 29" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M1.9673 14.1924L14.9422 1.37269C15.2613 1.05741 15.2613 0.551755 14.9422 0.236466C14.6231 -0.0788221 14.1113 -0.0788221 13.7922 0.236466L0.239328 13.6273C-0.0797759 13.9426 -0.0797759 14.4482 0.239328 14.7635L13.7922 28.1484C13.9487 28.3031 14.1595 28.3864 14.3642 28.3864C14.5689 28.3864 14.7796 28.309 14.9362 28.1484C15.2553 27.8331 15.2553 27.3275 14.9362 27.0122L1.9673 14.1924Z" fill="white"/>
      </svg>
    </div>
  )
}

class Home extends Component{
    constructor(props) {
        super(props);
        this.state = {
          viewCompleted: true,
          ProductList: [],
          modal: false,
          activeItem: {
            title: '',
            cost: ''
          },

          catalog: [
            {title: 'Квадроциклы', img: c1, to: '/atv'},
            {title: 'Гидроциклы',  img: c2, to: '/watercraft'},
            {title: 'Катера',      img: c3, to: '/boat'},
            {title: 'Снегоходы',   img: c4, to: '/snowmobile'},
            {title: 'Вездеходы',   img: c5, to: '/vehicle'},
            {title: 'Двигатели',   img: c6, to: '/motor'}],
          
          slider: [
            {img: slider},
            {img: slider},
            {img: slider},
            {img: slider},
            {img: slider},
            {img: slider}
          ],
        }
      }
    
      componentDidMount() {
        this.refreshList()
      }
    
      refreshList = () => {
        axios
         .get('/api/product/')
         .then((res) => this.setState({ ProductList: [...this.state.ProductList, ...res.data] }))
         .catch((err) => console.log(err))
      }

    render() {
        const sliderSettings = {
          dots: true,
          infinity: true,
          speed: 500,
          slidesToShow: 1,
          slidesToScroll: 1,
          nextArrow: <CustomNextArrow />,
          prevArrow: <CustomPrevArrow />
        }

        return(
            <div style={{textAlign: 'center'}} className='Home'>
              <div className="container">
                <div className="intro">
                  <SliderUI wrapperClass="slider" settings={sliderSettings} sliderItemClass='slider_item' sliderItems={this.state.slider} />
                </div>
                
                <form className="search">
                  <div className="label">
                    <label htmlFor="searchHome">Поиск по названию товара</label>
                  </div>
                  <div className="form">
                    <input type="text" id="searchHome" placeholder='Введите название товара' />
                    <button>ИСКАТЬ</button>
                  </div>
                </form>
                
                
                {/* <div>
                    {this.state.ProductList.map((product, index) => (
                        <p key={index}>{product.title}</p>
                    ))}
                </div> */}


                <div className="catalog">
                  { this.state.catalog.map((catalogItem, index) => (
                    <NavLink className="catalog_item" to={ catalogItem.to } key={ index }>
                      <div className="left-side">
                        <h1>{ catalogItem.title }</h1>
                        <p>
                          <span>Подробнее</span>
                            <svg width="6" height="9" viewBox="0 0 6 9" fill="none" xmlns="http://www.w3.org/2000/svg">
                              <path d="M0.228824 7.88793C-0.0650263 8.13366 -0.0762935 8.54196 0.203658 8.79989C0.48361 9.05782 0.948767 9.06771 1.24262 8.82198C1.24262 8.82198 5.77719 4.97116 5.78955 4.95998C6.07934 4.69388 6.06851 4.27195 5.76535 4.01758L1.24266 0.178763C0.949277 -0.067399 0.484101 -0.0581923 0.203658 0.199327C-0.0767846 0.456846 -0.0662956 0.865161 0.227086 1.11132L3.71295 4.12125C3.94389 4.32066 3.94393 4.67861 3.71304 4.87807L0.228824 7.88793Z" fill="#C4C4C4"/>
                            </svg>
                        </p>
                      </div>
                      <img src={ catalogItem.img } alt='catalogItem' />
                    </NavLink>
                  )) }
                </div>
                <NavLink to='/motor' className="add">
                  <img src={ add } alt="add" />
                  <p className="text">
                    <span>СКИДКИ</span>
                    на все двигатели <br /> до 70%
                  </p>
                  <NavLink to='/motor'>ПОСМОТРЕТЬ ВСЕ</NavLink>
                </NavLink>
              </div>
            </div>
        )
    }
}

export default Home