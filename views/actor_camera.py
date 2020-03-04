from views.area_media import AreaMedia


class ActorCamera(AreaMedia):

    def __init__(self, focus_key, point_camera):
        self.focus_key = focus_key
        self.point_camera = point_camera

    def to_point_camera(self):
        return self.point_camera

    def render(self):
        self.point_camera.render()

    def with_area(self, area):
        focused_camera = area.print_to(self).to_point_camera()
        return area.print_to(focused_camera)

    def with_actor(self, x, y, key):
        return ActorCamera(self.focus_key, self.point_camera.move_to(x, y)) if self.focus_key == key else self


