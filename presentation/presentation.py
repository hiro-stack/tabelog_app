from collections import Counter


class Presentation:

    def __init__(self):
        self._time_is: str = ""
        self._price_max: int = 0
        self._max_minutes: int = 0
        self._menus: list[str] = []
        self._weight: dict[str, float] = {}

        # {"名前": 重要度} を保存する辞書
        self._people_importance_scores: dict[str:int] = {}

        # 投票結果　例：{"食べ物": [0.5, 0.25, 0.25]}
        self._votes_result = {}

        # 公平性のパラメーター(0: 重要度重視, 1: 多数決重視)
        self._alpha: float = 0

    def app(self):
        # データのインプット
        self.data_input()
        self.determine_weight()
        print("data_input_ok!!")

        # データの確認
        print(self._max_minutes)
        print(self._price_max)
        print(self._time_is)
        print(self._weight)
        print(self._people_importance_scores)
        print(self._votes_result)
        print(self._alpha)

    def data_input(self):
        # 入力値の設定
        self.determin_importance()
        self._time_is = input("dinner or lunch:")
        self._price_max = self.get_valid_input("予算の上限", int)
        self._max_minutes = self.get_valid_input("現在地から徒歩何分以内か", int)

    def get_valid_input(self, prompt: str, input_type: type) -> int:
        while True:
            try:
                return input_type(input(prompt))
            except ValueError:
                print(f"{prompt}には適切な{input_type.__name__}を入力してください。")

    def determin_importance(self):
        print("=== 公平性のパラメーターを設定してください ===")
        self._alpha = float(
            input(
                "公平性パラメータ (0: 個人の決定の重要度重視するか？, 1: 多数決を重視するか？)→"
            )
        )
        self.determin_people_importance()
        self.determin_food_importance()

    def determin_people_importance(self):
        print("=== グループの重要度と投票内容を入力してください ===")
        num_people = int(input("グループの人数を入力してください: "))

        for i in range(num_people):
            name = input(f"メンバー {i + 1} の名前を入力してください: ")

            if self._alpha == 1:
                importance = 0.5  # 全員の重要度を 0.5 に設定
                print(f"{name} さんの決定権の重要度を自動的に 0.5 に設定しました。")
            else:
                importance = float(
                    input(
                        f"{name} さんの決定権の重要度を 0~1 の間で入力してください (例: 0.5): "
                    )
                )

            self._people_importance_scores[name] = importance

    # 投票内容を入力
    def determin_food_importance(self):

        print("(異なる人が同じ種類の食べ物を選んだとしても反映できます)")
        for name, importance in self._people_importance_scores.items():
            choice = input(
                f"{name} さんが食べたいものを入力してください (例: ラーメン): "
            )

            if choice not in self._votes_result:
                self._votes_result[choice] = []

            self._votes_result[choice].append(importance)

    def data_maked(self):
        self._menus = list(set(self._menus))

    def determine_weight(self):
        print(
            "[現在地からの近さ], [予算], [評価], [声の大きさ]の重みづけの設定(グループの特徴や状況に応じて項目ごとに重みづけ)"
        )

        print("それぞれの項目は0～1の間で重みづけをする")

        print(
            """項目の重みづけの例:
              記念日や特別な日
              
              シチュエーション概要:
              誕生日、結婚記念日、接待など特別な意味を持つ場面。
              全体の雰囲気やクオリティが最重要。
              
              根拠:
              - 評価 (evaluate): 特別な場面では、クオリティの高い店が必須。
              - 価格 (budget): 高めの価格も許容範囲。
              - 徒歩時間 (distance): 遠くても価値があれば妥協できる。
              - 声の大きさ (voice_force): ホストや主催者の食べたいものの意向は重視。
              
              重み付け:
              「現在地点の近さ」の項目の重みづけ: 1.5,   # 星評価を最優先。
              「予算」の項目の重みづけ: 0.8     # 価格は妥協。
              「お店の評価」の項目の重みづけ: 0.9,   # 徒歩時間は重要度低め。
              「声の大きさ」の項目の重みづけ: 1.0 # 食べたいものの意見の反映度合いはそこそこ重要
              """
        )

        force1 = float(input("「現在地点の近さ」の項目の重みづけ:"))
        force2 = float(input("「予算」の項目の重みづけ:"))
        force3 = float(input("「お店の評価」の項目の重みづけ:"))
        force4 = float(input("「声の大きさ」の項目の重みづけ"))
        self._weight = {
            "distance": force1,
            "budget": force2,
            "evaluate": force3,
            "voice_force": force4,
        }

    @property
    def menus(self):
        menus = list(self.votes_result.keys())
        return menus

    @property
    def max_minutes(self):
        return self._max_minutes

    @property
    def price_max(self):
        return self._price_max

    @property
    def time_is(self):
        return self._time_is

    @property
    def weight(self):
        return self._weight

    @property
    def votes_result(self):
        return self._votes_result

    @property
    def alpha(self):
        return self._alpha

    def main(self):
        self.app()


if __name__ == "__main__":
    presentation = Presentation()
    presentation.main()
