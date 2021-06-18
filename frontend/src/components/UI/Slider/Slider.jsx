import React from 'react'
import Slider from 'react-slick'

const SliderUI = props => (
    <Slider {...props.settings} className={props.wrapperClass}>
        {
            props.sliderItems.map((item, index) => (
                <div className={props.sliderItemClass} key={ index }>
                    <img src={ item.img } alt="now" />
                </div>
            ))
        }
    </Slider>
)

export default SliderUI