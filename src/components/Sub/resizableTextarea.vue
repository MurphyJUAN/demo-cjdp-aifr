
<script>

export default {
  name: 'resizableTextarea',
  data() {
    return {
      old_target_scrollHeight: 0,
    };
  },
  props: {
    outerElement: HTMLUListElement,
  },
  methods: {
    resizeTextarea (event) {
      // console.log("resizeTextarea")
      let old_scrollHeight = this.outerElement.scrollHeight;
      let old_scrollTop = this.outerElement.scrollTop;
      let new_scrollHeight = 0;
      let new_scrollTop = 0;
      let elementTopOffset = 0;
      let divTopOffset = 0;
      let elementRelativeTop = 0;
      let elementHeight = 0;
      let divHeight = 0;
      let diffHeight = 0;

      // apply new scroll height to current input textarea
      event.target.style.height = 'auto';
      event.target.style.height = (event.target.scrollHeight + 2) + 'px';


      // calculate height diff between new scroll height and old scroll height
      new_scrollHeight = this.outerElement.scrollHeight;
      diffHeight = (new_scrollHeight - old_scrollHeight);


      // calculate relative element top
      elementTopOffset = event.target.offsetTop;
      divTopOffset = this.outerElement.offsetTop;
      elementRelativeTop = elementTopOffset - divTopOffset;

      // get element new scroll height and div visible height
      elementHeight = event.target.scrollHeight;
      divHeight = this.outerElement.clientHeight;

      // calculate bottom diff between div and element
      let elementBottom = elementRelativeTop + elementHeight;
      let divBottom = diffHeight + old_scrollTop + divHeight;
      let diffBottom = divBottom - elementBottom;

      // calculate top diff between div and element
      let elementTop = elementRelativeTop;
      let divTop = diffHeight + old_scrollTop;
      let diffTop = elementTop - divTop;

      // console.log(diffTop)
      // console.log(diffHeight)
      if (diffTop < 10) {
        // check if diffBottom is negative, if yes, stick to bottom line
        if (diffTop < -35 && diffBottom < 0){
          // stick to bottom line
          new_scrollTop = diffHeight * 1 + old_scrollTop ;
        } else {
          // stick to top line
          new_scrollTop = diffHeight * 0 + old_scrollTop ;
        }

      }else if (elementHeight < divHeight){
        // check if backspace or delete lines, if yes, diffHeight will be negative
        if (diffHeight < 0 ) {
          // stick to top line
          new_scrollTop = diffHeight * 0 + old_scrollTop ;
        }else {
          // extend to both side
          new_scrollTop = diffHeight * 0.5 + old_scrollTop ;
        }
      }else {
        if (diffHeight < 0) {
          // stick to top line
          new_scrollTop = diffHeight * 0 + old_scrollTop ;
        }else {
          if (diffTop < 0){
            // stick to top line
            new_scrollTop = diffHeight * 0 + old_scrollTop ;
          } else {
            // stick to bottom line
            new_scrollTop = diffHeight * 1 + old_scrollTop ;
          }
        }
      }

      // console.log(diffBottom)
      if (diffBottom >= -50 && diffBottom < 10) {
        // check if backspace or delete lines, if yes, diffHeight will be negative
        if (diffHeight < 0) {
          // stick to top line
          new_scrollTop = diffHeight * 0 + old_scrollTop ;
        }else {
          // stick to bottom line
          new_scrollTop = diffHeight * 1 + old_scrollTop ;
        }
      }

      this.outerElement.scrollTop = new_scrollTop;
    },
  },
  mounted () {
    this.$el.addEventListener('input', this.resizeTextarea)
  },
  beforeDestroy () {
    this.$el.removeEventListener('input', this.resizeTextarea)
  },
  render () {
    this.$nextTick(() => {
      // console.log("render")
      let old_scrollHeight = this.outerElement.scrollHeight;
      let old_scrollTop = this.outerElement.scrollTop;
      let new_scrollHeight = 0;
      let new_scrollTop = 0;

      this.$el.setAttribute('style', 'height:' + 'auto');
      this.$el.setAttribute('style', 'height:' + (this.$el.scrollHeight + 2) + 'px;overflow-y:auto;resize:none;');


      this.outerElement.scrollTop = old_scrollTop;
    })
    return this.$slots.default[0]
  },
};

</script>